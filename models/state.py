#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from base_model import BaseModel, Base
from os import getenv
from models import storage, City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") is "file":
        @property
        def cities(self):
            '''getter for cities'''
            list_cities = []
            cities_dict = storage.all(City)
            for city in cities_dict.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
    else:
        cities = relationship("City", backref="state", cascade="all, delete")
