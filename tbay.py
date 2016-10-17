from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey

#will talk directly to db using raw SQL
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
#equivalent to pyscopg cursor - allows you to quee up and exec db transactions
Session = sessionmaker(bind=engine)
session = Session()
#acts like repository for the models
Base = declarative_base()

#Subclassing base registers the Item model w the declarative base
#when asking for the tables to be created, the Item table will be included.
class Item(Base): 
    __tablename__ = "items" #names the items in db

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Bid(Base):
    __tablename__ = "bids" 
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
Base.metadata.create_all(engine)