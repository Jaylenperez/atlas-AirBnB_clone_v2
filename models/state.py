#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database.
    Inherits from SQLAlchemy Base and links to MySQL table states.
    """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute for cities if storage is not DBStorage."""
            listofcities = []
            if models.storage_t != "db":
                for city in models.storage.all(City).values():
                    if city.state_id == self.id:
                        listofcities.append(city)
            return listofcities
