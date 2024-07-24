

import asyncio

from sqlalchemy import text
from app.factories import *
from app.database import sync_session_maker
from sqlalchemy.ext.asyncio import AsyncSession

def generate_fake_data():
    with sync_session_maker() as session:
            # Создаём таблицы и заполняем их тестовыми данными
            # Проверьте, что данные не существуют перед созданием
            result = session.execute(text('SELECT 1 FROM passengers LIMIT 1'))
            if result.scalar() is None:


                # Устанавливаем сессию для всех фабрик
                UserFactory._meta.sqlalchemy_session = session
                AirportFactory._meta.sqlalchemy_session = session
                AirlineFactory._meta.sqlalchemy_session = session
                FlightFactory._meta.sqlalchemy_session = session
                PassengerFactory._meta.sqlalchemy_session = session
                TicketWithPassengerFactory._meta.sqlalchemy_session = session
                SeatFactory._meta.sqlalchemy_session = session

                # Очищаем сессию от предыдущих объектов, если это необходимо
                session.expunge_all()


                users = UserFactory.create_batch(100)
                booked_tickets = TicketWithPassengerFactory.create_batch(150)
                seat = SeatFactory.create_batch(100)
                

                print("Mock data initialized.")
            else:
                print("Mock data already exists.")
