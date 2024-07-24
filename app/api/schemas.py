import datetime
from typing import Optional
from enum import Enum
from fastapi import Query
from pydantic import BaseModel

class PassengerType(str, Enum):
    ADULT = "adult"
    CHILDREN = "children"
    BABY = "baby"

class FlightGrade(str, Enum):
    ECONOMY = 'economy'
    COMFORT = 'comfort'
    BUSINESS = 'business'
    FIRST_CLASS = 'first_class'

class AirlineResponse(BaseModel):
    airline_id: int
    name: str
    logo_url: str

class AirportResponse(BaseModel):
    name: str
    country: str
    city: str
    airport_code: str

class FlightResponse(BaseModel):
    departure: datetime.datetime
    arrival: datetime.datetime
    flight_duration: datetime.timedelta
    airline: AirlineResponse
    origin: AirportResponse
    destination: AirportResponse

    class Config:
        model_config = {'from_attributes': True}

class PassengerResponse(BaseModel):
    id: int
    passenger_type: PassengerType
    first_name: str
    last_name: str
    email: str
    phone: str

    class Config:
        model_config = {'from_attributes': True}

class SeatResponse(BaseModel):
    flight: FlightResponse
    flight_grade: FlightGrade
    is_available: bool = True
    row_number: int
    column_number: str
    seat_number: str

    class Config:
        model_config = {'from_attributes': True}

class TicketResponse(BaseModel):
    ticket_id: int
    flight_grade: FlightGrade
    baggage_weight: int
    baggage_price: float
    ticket_price: float
    flight: FlightResponse

    class Config:
        model_config = {'from_attributes': True}


class SearchParams(BaseModel):
    origin: Optional[str] = Query(None, description="Origin of the flight")
    destination: Optional[str]= Query(None, description="Destination of the flight")
    departure: Optional[datetime.datetime] = Query(datetime.datetime.now(datetime.UTC), ge=datetime.datetime.now(datetime.UTC), description="Departure time")
    adults: Optional[int] = Query(0, description="Number of adults")
    children: Optional[int] = Query(0, description="Number of children")
    babies: Optional[int] = Query(0, description="Number of babies")
    flight_grade: Optional[str] = Query('economy', description="Class type")
    skip: Optional[int] = Query(0, description="Number of records to skip")
    limit: Optional[int] = Query(10, description="Number of records to return")