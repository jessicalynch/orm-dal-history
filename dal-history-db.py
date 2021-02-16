import pandas
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

# Load MySQL settings
USERNAME = os.getenv('MYSQL_USERNAME')
PASSWORD = os.getenv('MYSQL_PASSWORD')
db_name = 'airline_history'

# Configure SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/{db_name}', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)

# Create data models
class Airline(Base):
    """An individual airline that has many historical events"""
    __tablename__ = 'airlines'
    __table_args__ = {'schema':f'{db_name}'}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    iata_code = Column(String(length=2))

    def __repr__(self):
        return f'<Airline(name"{self.name}", IATA carrier code="{self.iata_code}">'

class Event(Base):
    """An individual event belonging to one airline"""
    __tablename__ = 'events'
    __table_args__ = {'schema':f'{db_name}'}

    id = Column(Integer, primary_key=True, nullable=False)
    airline_id = Column(Integer, ForeignKey(f'{db_name}.airlines.id'), nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(length=500), nullable=False)

    airline = relationship("Airline")

    def __repr__(self):
        return f'<Event(id="{self.id}" airline id="{self.airline_id}" year="{self.year}", description="{self.description}">'

# Insert sample data 
data_to_insert = [('airlines.csv', Airline), ('events.csv', Event)]
for data in data_to_insert:
    filename = 'data/' + data[0]
    model = data[1]
    dataframe = pandas.read_csv(filename)
    dataframe.to_sql(con=engine, name=model.__tablename__, if_exists='append', index=False)

# Confirm data was inserted
session = sessionmaker()
session.configure(bind=engine)
s = session()

airline_records = s.query(Airline).order_by(Airline.iata_code).all()
for record in airline_records:
    print(record)

event_records = s.query(Event).order_by(Event.year).limit(5) 
for record in event_records:
    print(record)
