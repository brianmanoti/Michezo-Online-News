#!/usr/bin/env python3
"""Class for players"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import CheckConstraint, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Player(BaseModel, Base):
	"""Player.

	Attributes:
		name(str)
		age(int)
		height(int): cm
		team(str)
		jersey(int)
		player_id(str)
		nationality(str)
		strong_foot(str)
	"""
	if models.storage_t == 'db':
		__tablename__ = 'players'
		jersey = Column(Integer, primary_key = True, nullable = False)
		name = Column(String(128), nullable = False)
		age = Column(Integer, nullable = False, CheckConstraint('age>=0') """Ensure age is not negative or null"""
		height = Column(Integer, nullable = False)
		nationality =  Column(String(128), nullable = False)
		strong_foot = Column(String(128), nullable = False)

		"""Foreign key relationship to 'teams' table"""
		team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
		"""Relationship with Team model"""
		teams = relationship("Team", back_populates="players")
	else:
		jersey=""
		name=""
		age=""
		height=""
		nationality=""
		strong_foot=""

	def __init__(self, *args, **kwargs):
		"""Initialize players class"""
		super().__init__(*args, **kwargs)
