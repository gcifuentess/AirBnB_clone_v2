#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"), primary_key=True,
                                 nullable=False),
                          Column("place_id", String(60),
                                 ForeignKey("places.id"), primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey('cities.id', ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_list = []

    if getenv("HBNB_TYPE_STORAGE") is "FileStorage":

        @property
        def amenities(self):
            """list of ids of the amenities related with the place"""
            # from models import storage
            return self.amenity_list

        @amenities.setter
        def amenities(self, obj):
            """populates the amenity_list """
            if (type(obj) is Amenity and
                obj.id not in self.amenity_list):
                self.amenity_list.append(obj.id)

        @property
        def reviews(self):
            """dict of reviews related with the place"""
            # from models import storage
            reviews_dict = {}
            for key, value in storage.all().items():
                if value.place_ide == self.id:
                    reviews_dict[key] = value
            return reviews_dict

    else:
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)

        reviews = relationship("Review", cascade="all,delete",
                               backref=backref("place", cascade="all,delete"),
                               passive_deletes=True)
