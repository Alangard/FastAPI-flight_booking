import datetime
import enum
from typing import List

from sqlalchemy import and_, func, select
from sqlalchemy.orm import aliased

from app.api.models import Ticket, Flight, Airport, Airline, Passenger, Seat
from app.api.schemas import AirlineResponse, AirportResponse, PassengerResponse, SearchParams, TicketResponse, FlightResponse
from sqlalchemy.ext.asyncio import AsyncSession


async def search_tickets(session: AsyncSession, params: SearchParams) -> List[TicketResponse]:

    departure_airport_alias = aliased(Airport)
    arrival_airport_alias = aliased(Airport)
    seat_alias = aliased(Seat)
    
    # Подзапрос для доступных мест
    seat_subquery = (
        select(
            Seat.flight_id,
            func.count().label('available_seats')
        )
        .filter(
            Seat.is_available == True,
            Seat.flight_grade == params.flight_grade.upper()
        )
        .group_by(Seat.flight_id)
        .subquery()
    )

    print(params)

    query = (
        select(
            Ticket.id.label('ticket_id'),
            Ticket.baggage_weight,
            Ticket.baggage_price,
            Ticket.ticket_price,
            Flight.departure,
            Flight.arrival,
            (Flight.arrival - Flight.departure).label('flight_duration'),
            Airline.id.label('airline_id'),
            Airline.name.label('airline_name'),
            Airline.logo_url,
            departure_airport_alias.name.label('departure_airport_name'),
            departure_airport_alias.country.label('departure_airport_country'),
            departure_airport_alias.city.label('departure_airport_city'),
            departure_airport_alias.code.label('departure_airport_code'),
            arrival_airport_alias.name.label('arrival_airport_name'),
            arrival_airport_alias.country.label('arrival_airport_country'),
            arrival_airport_alias.city.label('arrival_airport_city'),
            arrival_airport_alias.code.label('arrival_airport_code'),
            Passenger.id.label('passenger_id'),
            Passenger.passenger_type,
            Passenger.first_name,
            Passenger.last_name,
            Passenger.email,
            Passenger.phone,
        )
        .join(Flight, Ticket.flight_id == Flight.id)
        .join(Airline, Flight.airline_id == Airline.id)
        .join(departure_airport_alias, Flight.departure_airport_id == departure_airport_alias.id)
        .join(arrival_airport_alias, Flight.arrival_airport_id == arrival_airport_alias.id)
        .outerjoin(Passenger, Ticket.passenger_id == Passenger.id)
        .join(seat_subquery, Flight.id == seat_subquery.c.flight_id)
        .filter(
            (params.origin is None or departure_airport_alias.city == params.origin),
            (params.destination is None or arrival_airport_alias.city == params.destination),
            (params.departure is None or Flight.departure >= params.departure),
            seat_subquery.c.available_seats >= (params.adults + params.children + params.babies),
            Passenger.id.is_(None)
        )
        .offset(params.skip)
        .limit(params.limit)
    )

    result = await session.execute(query)
    rows = result.fetchall()

    tickets = []

    for row in rows:
        flight = FlightResponse(
            departure=row.departure,
            arrival=row.arrival,
            flight_duration=row.flight_duration,
            airline=AirlineResponse(
                airline_id=row.airline_id,
                name=row.airline_name,
                logo_url=row.logo_url,
            ),
            origin=AirportResponse(
                name=row.departure_airport_name,
                country=row.departure_airport_country,
                city=row.departure_airport_city,
                airport_code=row.departure_airport_code,
            ),
            destination=AirportResponse(
                name=row.arrival_airport_name,
                country=row.arrival_airport_country,
                city=row.arrival_airport_city,
                airport_code=row.arrival_airport_code,
            )
        )

        ticket = TicketResponse(
            ticket_id=row.ticket_id,
            flight_grade=params.flight_grade,
            baggage_weight=row.baggage_weight,
            baggage_price=row.baggage_price,
            ticket_price=row.ticket_price,
            flight=flight,
        )

        tickets.append(ticket)

    # Преобразование результатов в схемы
    ticket_responses = [TicketResponse.model_validate(ticket) for ticket in tickets]
    return ticket_responses
    
