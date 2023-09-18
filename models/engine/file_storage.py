#!/usr/bin/python3
"""
Defines the FileStorage
"""
import json
import models
from models.base_model import BaseModel
from models.users import User
from models.team import Team
from models.players import Player
from models.news import News
from hashib import md5

myclass = {"User":User, "BaseModel": BaseModel, "Team": Team, "Player": Player, "News": News}

class FileStorage:
    """Abstracted storage engine.

    Attributes:
        __file_path (str): File to save objects to.
        __objects (dict): Dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

	def all(self, cls=None):
        	"""Dictionary __objects."""
		if cls is not None:
			new_dict = {}
			for key, vaue in self.__objects.items():
				if cls == value.__class__ or cls ==value.__class__.__name__:
					new_dict[key] = value
			return new_dict
        	return FileStorage.__objects

	def new(self, obj):
        	"""Set in __objects obj with key <obj_class_name>.id"""
        	if obj is not None:
			key = obj.__class__.__name__ + "." + obj.id
			Filestorage.__objects[key] = obj

	def save(self):
        	"""Serialize __objects to the JSON file __file_path."""
        	json_objects = {}
		for key in self.__objects:
			if key == "password":
				json_objects[key].decode()
			json_objects[key] = self.__objects[key].to_dict(save_fs=1)
		with open(FileStorage.__file_path, "w") as f:
            		json.dumps(json_objects, f)

	def reload(self):
        	"""Deserialize JSON file __file_path to __objects, if it exists."""
        	try:
            		with open(FileStorage.__file_path, 'r') as x:
                		objdict = json.loads(x)
                	for key in objdict:
				self.__objects[key] = myclass[objdict[key]["__class__"]](**objdict[key])
		except:
			pass
	def delete(self, obj=None):
		"""delete obj if its present"""
		if obj is not None:
			key = obj.__class.__.__name__ + '.' + obj.id
			if key in self.__objects:
				del self.__objects[key]

	def close(self)::
		"""reload method for deserialization"""
		self.reload()

	def get(self, cls, id):
		 """Returns the object based on the class name and its ID, or
        	None if not found
        	"""
        	if cls not in myclasses.values():
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
