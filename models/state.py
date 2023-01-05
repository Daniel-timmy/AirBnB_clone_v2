#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = \
        relationship("City", backref='state', cascade='all, delete, delete-orphan')
    @property
    def cities(self):
        """returns a list of City instances"""
        city_dict = storage.all(City)
        city_result = []
        for key in city_dict:
            if city_dict[key].state_id == self.id:
                city_result.append(city_dict[key])
        return city_result
