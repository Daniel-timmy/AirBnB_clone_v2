#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import HBNB_TYPE_STORAGE


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    state_id = Column(String(60), nullable=False)
    name = Column(String(128), ForeignKey('state.id'), nullable=False)
    places = \
        relationship("Place",
                     backref="cities",
                     cascade='all, delete, delete-orphan')

