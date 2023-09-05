#!/usr/bin/env python3
"""Team class"""

from models.base_model import BaseModel

class Team(BaseModel):
	"""Team.

	team_name(str)
	team_nickname(str)
	stadium(str)
	city(str)
	coach(str)
	players(str)
	"""

	team_name=""
	team_nickname=""
	stadium=""
	city=""
	coach=""
	players=""
