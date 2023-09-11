#usr/bin/env python3
"""Class for players"""
from models.base_model import BaseModel

class Player(BaseModel):
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
	first_name=""
	last_name=""
	age=""
	height=""
	team=""
	player_id=""
	jersey=""
	strong_foot=""
