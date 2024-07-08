#!/usr/bin/python3
"""State Module for HBNB project."""
import models
from models.city import City, storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class."""

    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")


        @property
        def cities(self):
            """Getter attribute for cities."""
            listofcities = []

            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    listofcities.append(city)
            return listofcities
