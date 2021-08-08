from datetime import date
import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 


Base = declarative_base()
 

 
class Trends(Base):
    __tablename__ = 'trends'
    id = Column(Integer, primary_key=True)
    tag_order = Column(Integer)
    country_name = Column(String)
    tag_name = Column(String(250))
    date_trend = Column(String)
    time_trend = Column(String)

 
engine = create_engine('sqlite:///trends.db')
 

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
 


 

def take_hour():
    the_time = datetime.datetime.now()
    result = f"{the_time.hour}:{the_time.minute}"
    return result

def take_date():
    the_date = datetime.date.today()
    return str(the_date)

def save_to_db(any_dict):
    the_time = take_hour()
    the_date = take_date()
    
    for country in any_dict:
        count = 1
        counry_tags = any_dict[country]
        for tags in counry_tags:
            new_trend = Trends(tag_order=count, country_name=country, tag_name=tags, date_trend=the_date, time_trend=the_time)
            session.add(new_trend)
            count += 1
        session.commit()

