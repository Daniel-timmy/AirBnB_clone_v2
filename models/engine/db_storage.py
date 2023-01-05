#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from sqlalchemy import (create_engine)
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session, relationship


class DBStorage:
    '''database storage engine for mysql storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate new dbstorage instance'''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""

        dict_result = {}
        classes = {'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

        if cls is None:
            for item in classes:
                obj = self.__session.query(classes[item]).all()
                c_name = classes[item].__name__
                for obj_d in obj:
                    c_name = c_name + '.' + obj_d.id
                    dict_result[c_name] = obj_d

        elif cls in classes:
            c_name = cls.__name__
            obj = self.__session.query(cls).all()
            for obj_d in obj:
                c_name = c_name + '.' + obj_d.id
                dict_result[c_name] = obj_d

        return dict_result

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
