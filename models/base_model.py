"""Parent file from which all files will inherit from"""
import uuid
from models import storage
from datetime import datetime

class BaseModel:
"""Parent Class"""

	def __init__(self, *args, **kwargs**):
		"""instantiate a unique id, and time stamps for the time a user is created and updated"""
		self.created_at=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
		self.updated_at=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
		self.id=str(uuid.uuid4())
		
		if len(kwargs)!=0;
			for x,y in kwargs.items():
				if x=="created_at" or x=="updated_at":
					self.__dict__[x]=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
				else:
					self.__dict__[x]=y
		else:
			storage.new(self)

	def save_update(self)
		self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
		storage.save()
	def save_to_dict(self):
		rdict=self.__class__.copy()
		rdict["created_at"]=self.created_at
		rdict["updated_at"]=self.updated_at
		rdict["__class__"]=self.__class__.__name__
	def __str__(self):
		return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)
