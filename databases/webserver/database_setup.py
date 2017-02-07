"""
Configuration: import all the necessary modules.
                creates instance of declarative base,
                connects the database and adds tables and columns.
Class: represent data in Python.
Table: represent the specific table in database.
Mapper: connect the columns of table to the class that
        represents it.
"""
# ---------------------------------
# ########Configuration##########
# ---------------------------------
#sys module provides a number of functions and variables that can
#be used for different part of the Python run-time environment.
import sys
import os

# handy for writing the mapper code.
from sqlalchemy import Column, ForeignKey, Integer, String

#use in the configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#in order to create foreign key relationships, use in mappper
from sqlalchemy.orm import relationship

#use in configuration file at the end of file
from sqlalchemy import create_engine

#make an instance of the declarative_base class we just imported.
#declarative_base will let sqlalchemy know that our classes are
#sqlalchemy classes that correspond to tables in our database.
Base=declarative_base()


# ---------------------------------
# ########class##########
# ---------------------------------

#two classes correspondsto the two tables in our database.
#Restaurant and menu item.

class Restaurant(Base):
    #representation of table inside the database.
    # let sqlalchemy know the variable that we will use to refer
    #to our table: __tablename__='some_table'
    __tablename__='restaurant'
    name=Column(String(250),nullable=False)

    id=Column(Integer,primary_key=True)
    print __tablename__

class MenuItem(Base):
    #maps python objects to columns in the database
    #colunmName=Column(attributes,...)
    __tablename__='menu_item'

    name=Column(String(80),nullable=False)
    id=Column(Integer, primary_key=True)
    course=Column(String(250))
    description=Column(String(250))
    price=Column(String(8))
    restaurant_id=Column(Integer,ForeignKey('restaurant.id'))
    restaurant=relationship(Restaurant)

#####Insert at the end of file#####

#create an instance of our create_engine class and point to the database
#use SQLite 3
engine=create_engine('sqlite:///restaurantmenu.db')

#goes into the database and adds the classes as new tables in our databases.
Base.metadata.create_all(engine)
