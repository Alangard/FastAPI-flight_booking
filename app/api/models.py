import enum
import uuid
from datetime import datetime
from typing import Any, List, Optional

from sqlalchemy import Boolean, DateTime, Enum, Float,  ForeignKey,Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import TIMESTAMP
from app.database import BaseModel



class PassengerType(enum.Enum):
    ADULT = "adult"
    CHILDREN = "children"
    BABY = "baby"

class FlightGrade(enum.Enum):
    ECONOMY = 'economy'
    COMFORT = 'comfort'
    BUSINESS = 'business'
    FIRST_CLASS = 'first_class'


class Passenger(BaseModel):
    __tablename__ = "passengers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    phone: Mapped[str] = mapped_column(String)
    passenger_type: Mapped[PassengerType] = mapped_column(Enum(PassengerType))
    tickets: Mapped[List["Ticket"]] = relationship("Ticket", back_populates="passenger")

class Airport(BaseModel):
    __tablename__ = "airports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    country: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)
    code: Mapped[str] = mapped_column(String, unique=True, index=True)

    departure_flights: Mapped[List["Flight"]] = relationship("Flight", back_populates="departure_airport", foreign_keys="Flight.departure_airport_id")
    arrival_flights: Mapped[List["Flight"]] = relationship("Flight", back_populates="arrival_airport", foreign_keys="Flight.arrival_airport_id")

class Airline(BaseModel):
    __tablename__ = "airlines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    logo_url: Mapped[str] = mapped_column(String)

    flights: Mapped[List["Flight"]] = relationship("Flight", back_populates="airline")

class Seat(BaseModel):
    __tablename__ = "seats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    flight_id: Mapped[int] = mapped_column(Integer, ForeignKey("flights.id", ondelete='CASCADE'))
    flight_grade: Mapped[FlightGrade] = mapped_column(Enum(FlightGrade))
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    row_number: Mapped[int] = mapped_column(Integer)
    column_number: Mapped[str] = mapped_column(String)
    seat_number: Mapped[str] = mapped_column(String, index=True)

    flight: Mapped["Flight"] = relationship("Flight", back_populates="seats")


class Flight(BaseModel):
    __tablename__ = "flights"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    airline_id: Mapped[int] = mapped_column(Integer, ForeignKey("airlines.id", ondelete='CASCADE'))
    departure_airport_id: Mapped[int] = mapped_column(Integer, ForeignKey("airports.id", ondelete='CASCADE'))
    arrival_airport_id: Mapped[int] = mapped_column(Integer, ForeignKey("airports.id", ondelete='CASCADE'))
    departure: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True))
    arrival: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True))

    airline: Mapped["Airline"] = relationship("Airline", back_populates="flights")
    departure_airport: Mapped["Airport"] = relationship("Airport", foreign_keys=[departure_airport_id], back_populates="departure_flights")
    arrival_airport: Mapped["Airport"] = relationship("Airport", foreign_keys=[arrival_airport_id], back_populates="arrival_flights")
    tickets: Mapped[List["Ticket"]] = relationship("Ticket", back_populates="flight")
    seats: Mapped[List["Seat"]] = relationship("Seat", back_populates="flight")

class Ticket(BaseModel):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    flight_id: Mapped[int] = mapped_column(Integer, ForeignKey("flights.id", ondelete='SET NULL'))
    passenger_id: Mapped[int] = mapped_column(Integer, ForeignKey("passengers.id", ondelete='SET NULL'), nullable=True) 
    baggage_weight: Mapped[int] = mapped_column(Integer)
    baggage_price: Mapped[float] = mapped_column(Float)
    ticket_price: Mapped[float] = mapped_column(Float)

    flight: Mapped["Flight"] = relationship("Flight", back_populates="tickets")
    passenger: Mapped[Optional["Passenger"]] = relationship("Passenger", back_populates="tickets") 

