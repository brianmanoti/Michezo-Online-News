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
	def all(self, cls=None):
		"""update on current database session"""
		new_dict = {}
		for clss in classes:
			if cls is None or cls is classes[clss] or cls is clss:
				objs = self.__session.query(classes[clss]).all()
				for obj in objs:
					key = obj.__class__.__name__ + '.' + obj.id
					new_dict[key] = obj
		return (new_dict)
	def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

	def save(self):
        	"""commit all changes of the current database session"""
        	self.__session.commit()

	def delete(self, obj=None):
        	"""delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

	def reload(self):
        	"""reloads data from the database"""
        	Base.metadata.create_all(self.__engine)
        	sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        	Session = scoped_session(sess_factory)
        	self.__session = Session

	def close(self):
        	"""call remove() method on the private session attribute"""
        	self.__session.remove()

    	def get(self, cls, id):
        	"""
        	Returns the object based on the class name and its ID, or
        	None if not found
        	"""
        	if cls not in classes.values():
            		return None

        	all_cls = models.storage.all(cls)
        	for value in all_cls.values():
            		if (value.id == id):
                	return value

       		return None

	def count(self, cls=None):
        	"""
        	count the number of objects in storage
        	"""
        	all_class = classes.values()

        	if not cls:
			count = 0
            		for clas in all_class:
                		count += len(models.storage.all(clas).values())
        	else:
            		count = len(models.storage.all(cls).values())

        	return count
