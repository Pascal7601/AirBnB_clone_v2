#!/usr/bin/python3
"""
Place Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
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

    reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    if os.getenv('HBNB_STORAGE_TYPE') != 'db':
        # File-based storage properties and methods
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances"""
            from models import storage
            return [review for review in storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances"""
            from models import storage
            return [storage.get('Amenity', amenity_id) for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute that handles appending Amenity IDs"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)

