#usr/bin/env python3
""" News class """

import models
import sqlalchemy
from base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationships
from sqlalchemy import Column, String

class News(BaseModel):
	"""News

	Attributes:
		title(str)
		
	"""
	if models.storage_t == 'db':
		__tablename__ = 'News'
		title = Column(String=128, nullable=False)
	else:
		title=""

	def __init__(self, *args, **kwargs):
		"""Initializes News"""
		super().__init__(*args, **kwargs)
