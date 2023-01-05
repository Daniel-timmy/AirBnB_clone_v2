#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models import storage

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenities_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", backref='place', cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    @property
    def reviews(self):
        """returns the list of Review instances"""
        review_dict = storage.all(Review)
        review_result = []
        for item in review_dict:
            if review_dict[item].place_id == self.id:
                review_result.append(review_dict[item])
        return review_result

    @property
    def amenities(self):
        """returns the list of Amenity instances"""
        amenity_dict = storage.all(Amenity)
        amenity_result = []
        for key in amenity_dict:
            if amenity_dict[key].id in self.amenity_ids:
                amenity_result.append(amenity_dict[key])
        return amenity_result

    @amenities.setter
    def amenities(self, obj):
        """handles append method for adding
        an Amenity.id to the attribute amenity_ids."""
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
