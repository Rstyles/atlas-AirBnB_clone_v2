#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base, storage
from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy import Column
from sqlalchemy import String
import os
from sqlalchemy.orm import relationship

from models.review import Review


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def reviews(self):
            """Review Getter attribute in case of file storage"""
            reviews_list = []

            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """getter"""
            amenities_list = []

            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)

    else:
        reviews = relationship(
            "Review", backref="place", cascade="all, delete, delete-orphan"
        )
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            back_populates="place_amenities",
            viewonly=False,
        )
