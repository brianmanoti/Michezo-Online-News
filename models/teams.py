#!/usr/bin/env python3
"""Team class"""

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Team(BaseModel, Base):
	"""Team.

	id(int)
	team_name(str)
	team_nickname(str)
	stadium(str)
	city(str)
	coach(str)
	players(str)
	"""
	if models.storage_t == 'db':
		__tablename__ = 'teams'
		id = Column(Integer, primary_key=True, nullable=False)
		team_name = Column(String(60), nullable=False)
		team_nickname = Column(String(60), nullable=False)
		stadium = Column(String(60), nullable=False)
		city = Column(String(60), nullable=False)	
		coach = Column(String(60), nullable=False)
		"""Defines foreign key relationship"""
		players_id= Column(Integer, ForeignKey=('players.jersey'), nullable=False)
		"""Linking players to teams"""
		players = relationship("Player", back_populates="teams")
	else:
		id=""
		team_name=""
		team_nickname=""
		stadium=""
		city=""
		coach=""
		players=""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
