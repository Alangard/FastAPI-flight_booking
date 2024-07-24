import random
import uuid
import factory
from app.api.models import Passenger, Airport, Airline, Flight, Ticket, PassengerType, FlightGrade, Seat
from app.users.models import User
from app.database import sync_session_maker
from sqlalchemy.ext.asyncio import AsyncSession

# Фабрика для модели User
class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User

        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n + 1)  # Auto-incrementing id starting from 1
    guid = factory.LazyAttribute(lambda x: uuid.uuid4())  # Generate a new UUID for each user
    password = factory.Faker('password', length=12)  # Generate a random password with 12 characters
    first_name = factory.Faker('first_name')  # Generate a random first name
    last_name = factory.Faker('last_name')  # Generate a random last name
    phone_number = factory.Faker('phone_number')  # Generate a random phone number
    is_superuser = False
    user_image = factory.Faker('image_url')  # Generate a random image URL



# Фабрика для модели Passenger
class PassengerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Passenger

        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda obj: '%s@example.com' %(obj.first_name + str(obj.id)))
    phone = factory.Faker('phone_number')  # Generate a random phone number
    passenger_type = factory.Iterator([PassengerType.ADULT, PassengerType.CHILDREN, PassengerType.BABY])

# Фабрика для модели Airport
class AirportFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Airport

        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Airport %d' % n)
    country = factory.Faker('country')
    city = factory.Faker('city')
    code = factory.LazyAttribute(lambda obj: f'{obj.id} - {random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}')



# Фабрика для модели Airline
class AirlineFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Airline

        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda obj: 'airline%s@example.com' % obj.id)
    logo_url = factory.Faker('image_url')

# Фабрика для модели Flight
class FlightFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Flight

        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n)
    airline = factory.SubFactory(AirlineFactory)
    departure_airport = factory.SubFactory(AirportFactory)
    arrival_airport = factory.SubFactory(AirportFactory)
    departure = factory.Faker('date_time_between', start_date='now', end_date='+30d')
    arrival = factory.Faker('date_time_between', start_date='+1d', end_date='+31d')

    # Используйте RelatedFactoryList для создания связанных объектов Seat
    seats = factory.RelatedFactoryList(
        'app.factories.SeatFactory',  # Замените на правильный путь к вашей фабрике SeatFactory
        factory_related_name='flight',
        size=20  # Количество мест на рейс
    )


# Создайте фабрику для модели Seat
class SeatFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Seat

        sqlalchemy_session_persistence = 'commit'

    flight = factory.SubFactory(FlightFactory)
    flight_grade = factory.Iterator(FlightGrade)
    row_number = factory.Faker('random_int', min=1, max=50)
    column_number = factory.Faker('bothify', text='?', letters='ABCDEF')
    seat_number = factory.LazyAttribute(lambda obj: f"{obj.column_number}{obj.row_number}")

    # Определите вероятность занятости места
    @factory.lazy_attribute
    def is_available(self):
        return random.random() < 0.75  # 75% вероятность True





# Фабрика для модели Ticket
class TicketWithPassengerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Ticket

        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n)
    flight = factory.SubFactory(FlightFactory)
    baggage_weight = factory.Faker('pyint', max_value=30)
    baggage_price = factory.Faker('pyfloat', positive=True, max_value=100)
    ticket_price = factory.Faker('pyfloat', positive=True, max_value=30000)

    @factory.lazy_attribute
    def passenger(self):
        if random.random() < 0.75:  # 75% вероятность создания Passenger
            return PassengerFactory()
        return None
