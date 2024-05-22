#!/usr/bin/python3
"""
Place Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
import os


association_table = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)


class Place(BaseModel, Base):
    """ 
    A place to stay
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(128))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    amenity_ids = []

    if os.getenv('HBNB_STORAGE_TYPE') == 'db':
        reviews = relationship('Review', backref='place', 
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=association_table,
                                 back_populates='place_amenities', viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances"""
            from models import storage
            reviews_list = []
            for review in storage.all('Review').values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
       
        
        @property
        def amenities(self):
            from models import storage
            return [storage.get('Amenity', amenity_id) for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)

