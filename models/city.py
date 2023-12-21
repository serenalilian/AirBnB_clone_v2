#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
=======
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
>>>>>>> d2a36bc3e4ca57741bd6a3133870326e443d1671
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


<<<<<<< HEAD
class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""


=======
class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
>>>>>>> d2a36bc3e4ca57741bd6a3133870326e443d1671
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
