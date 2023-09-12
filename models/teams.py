#!/usr/bin/env python3
"""Team class"""

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationships


class Team(BaseModel):
	"""Team.

	team_name(str)
	team_nickname(str)
	stadium(str)
	city(str)
	coach(str)
	players(str)
	"""
	if models.storage_t == 'db':
		__tablename__ = 'teams'
		team_name = Column(String(128), nullable=False)
		team_nickname = Column(String(128), nullable=False)
		stadium = Column(String(128), nullable=False)
		city = Column(String(128), nullable=False)	
		coach = Column(String(128), nullable=False)
		players = Column(String(128), nullable=False)
		player = relationship("Player", backref="team")
	else:
		team_name=""
		team_nickname=""
		stadium=""
		city=""
		coach=""
		players=""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
