#!/usr/bin/python3
"""
dtabase storage
"""
from sqlalchemy import create_engine
from models.base_model import Base
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        db = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                      password,
                                                      host, db)
        
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        function to
        """
        obj_list = []
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                obj_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                obj_list.extend(self.__session.query(subclass).all())
        for obj in obj_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict
        

    def new(self, obj):
        """
        adds object to the session
        """
        self.__session.add(obj)


    def save(self):
        """
        saves a file to the database
        """
        self.__session.commit()


    def delete(self, obj=None):
        """
        deletes the object
        """
        if obj:
            self.__session.delete(obj)
        

    def reload(self):
        """
        reloads the database
        """
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()


    def close(self):
        """
        calls the remove method
        """
        self.__session.close()            












