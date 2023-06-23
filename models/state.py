#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Integer
from models.engine.file_storage import storage

class State(BaseModel, Base):
    """ State class """
    name = ""
