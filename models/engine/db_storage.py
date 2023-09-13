#!/usr/bin/env python3
"""Database Storage  Class"""

import sql alchemy
import models
from os import getenv
from models.news import News
from models.users import User
from models.players import Player
from models.teams import Team
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"News":News, "User":User,"Player": Player, "Team": Team}

class DBStorage:
	"""MySQL Database Interaction"""
	__engine = None
	__session = None

	def __init__(self):
		"""DBStorage Object Instantiation"""
		Michezo_MYSQL_USER = getenv('Michezo_MYSQL_USER')
		Michezo_MYSQL_PWD = getenv('Michezo_MYSQL_PWD')
		Michezo_MYSQL_HOST = getenv('Michezo_MYSQ_HOST')
		Michezo_ENV = getenv('Michezo_ENV')
		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(Michezo_MYSQL_USER,
                                             Michezo_MYSQL_PWD,
                                             Michezo_MYSQL_HOST,
                                             Michezo_MYSQL_DB))
		if Michezo_Env == 'test':
			Base.metadata.drop_all(self.engine)


