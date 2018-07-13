## Database for The Appointment Tracker Applciation ##
import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

## Customer Table ##
class Customer(Base):
    __tablename__='customers'
    id = Column(Integer, primary_key=True)               # Customer ID
    first_name = Column(String(250), nullable=False)     # Customer First Name
    last_name = Column(String(250), nullable=False)      # Customer Last Name
    time = Column(String(250), nullable=False)           # Customer Appointment Time


engine = create_engine('sqlite:///customer.db', echo = True)
Base.metadata.create_all(engine)
