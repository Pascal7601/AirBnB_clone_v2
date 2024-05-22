#!/usr/bin/python3
"""
State Module for HBNB project
 """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = Relationship('City', backref='state', 
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """
            property to handle file storage
            """
            import models
            from models.city import City

            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)