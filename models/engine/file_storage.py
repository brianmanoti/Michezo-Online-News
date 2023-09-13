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
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dumps(objdict, f)

    def reload(self):
        """Deserialize JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as x:
                objdict = json.loads(x)
                for i in objdict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
