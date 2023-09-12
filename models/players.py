#usr/bin/env python3
"""Class for players"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Player(BaseModel, Base):
	"""Player.

	Attributes:
		first_name(str)
		last_name(str)
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
		name = Column(String(128), nullable=False)
	else:
		first_name=""
		last_name=""
		age=""
		height=""
		team=""
		player_id=""
		jersey=""
		strong_foot=""

	def __init__(self, *args, **kwargs):
		"""Initialize players class"""
		super().__init__(*args, **kwargs)
