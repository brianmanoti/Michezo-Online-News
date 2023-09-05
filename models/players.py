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
		player_id(str)
	"""
	first_name=""
	last_name=""
	age=""
	height=""
	team=""
	player_id=""
