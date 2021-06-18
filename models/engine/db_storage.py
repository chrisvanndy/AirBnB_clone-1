#!/usr/bin/python3
"""define class"""
import os
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review}


class DBStorage:
    """DBStorage creates the engine connected to hbnb_dev_db"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              password,
                                              host,
                                              database),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """queries database, returns instances of class or all objects"""
        objects_dict = {}

        if cls is None:
            for classname in classes.values():
                for _cls in self.__session.query(classname):
                    key = _cls.__class__.__name__+'.'+_cls.id
                    objects_dict[key] = _cls
            return objects_dict
        else:
            if cls in classes.values():
                for _cls in self.__session.query(cls):
                    key = _cls.__class__.__name__+'.'+_cls.id
                    objects_dict[key] = _cls
            return objects_dict

    def new(self, obj):
        """adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """  """
        from sqlalchemy.orm import sessionmaker, scoped_session
        from sqlalchemy.orm.session import Session
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False,
                            autocommit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def close(self):
        """release connection/transactional resources of session"""
        self.__session.close()
