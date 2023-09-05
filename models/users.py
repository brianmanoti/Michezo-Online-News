#usr/bin/env python3
from models.base_model import BaseModel


class User(BaseModel):
	"""User Class
	Attributes:
		email(str)
		password(str)
		first_name(str)
		last_name(str)
	"""
	email=""
	password=""
	first_name=""
	last_name=""
