#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Integer
from models.engine.file_storage import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete')

    def cities(self):
        c_list = []
        c_dict = storage.all(City)
        for k, v in c.dict.items():
            if v.state_id == self.id:
				c_list.append(v)
		return c_list
