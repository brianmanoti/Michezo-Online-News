usr/bin/env python3
"""Creates User Class"""

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
	"""User Class
	Attributes:
		email(str)
		password(str)
		username(str)
		user_id(str)
	"""
	if models.storage_t == 'db':
		__tablename__ = 'users'
		user_id = Column(String(128), nullable=False)
		username= Column(String(60)), nullable=False)
		email = Column(String(60), unique=True, nullable=False)
		password = Column(String(20), nullable=False) 
	else:
		email = ""
		password = ""
		username = ""
		user_id = str(uuid.uuid4())

	def __init__(self, *args, **kwargs):
		"""user initialization"""
		super().__init__(*args,**kwargs)

	def __setattr__(self, name, value):
		"""sets encrypted password"""
		if name == "password":
			value = md5(value.encode()).hexidigest()
		super().__setattr__(name, value)
