#usr/bin/env python3
"""The console module"""

import sys
import cmd
import JSON
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.users import User
from models.team import Team
from models.players import Player
from models.news import News

class Michezo(cmd.Cmd):
	"""A class containing commands to control the Michezo site"""
	intro= "Welcome to Michezo Online News"
	prompt= '(Michezo) '
	classes=["Basemodel", "Users", "Teams", "Players", "News"]

	def do_quit(self, line):
		""" command to quit the program """
		return True

	def do_EOF(self, line):
		""" command to exit the program """
		return True
	def do_emptyline(self):
		""" no command """
		pass

	def do_create(self, classname):
		""" creates new instance """
		if len(classname)==0:
			print("class not provided")
		elif classname not in self.classes:
			print("class not present")
			return False
		else:
			new=eval("{}()".format(classname))
			new.save()
			print(new.id)
	def do_show(self, line):
		""" displays an instance of class """
		args=line.split()
		if len(args)==0:
			print("No classname provided")
			return False
		elif args[0] not in self.classes:
			print("Class not present")
			return False
		elif len(args) < 2:
			print("No ID present")
			return False
		else:
			objs=storage.all()
			for x in objs.keys():
				if x == "{}.{}".format(args[0], args[1]):					print(objs[x])
					return False
			print("No instance found")
	def do_destroy(self,line):
		""" Destroys an existing class instance and updates storage """
		args=line.split()
		if len(args)==0:
			print("No classname provided")
			return False
		elif args[0] not in self.classes:
			print("Class not present")
			return False
		elif len(args)<2:
			print("No ID present")
		else:
			objs=storage.all()
			for x in objs:
				if x == "{}.{}".format(args[0], args[1]):
					objs.pop(x)
					objs.save()
					return False
			print("No instance found")
	def do_all(self, line):
		""" Displays all instances """
		args=line.split()
		objs=storage.all()
		if len(args)==0:
			for x in objs:
				strarg=str(objs[x])
				print(strarg)
		elif args[0] not in self.classes:
			print("Class not present")
			return False
		else:
			for x in objs:
				if x.startswith(args[0]):
					strarg=str(objs[i])
					print(strarg)
		return False
	def do_update(self, line):
        	''' updates an instance based on class name and id'''
        	args = line.split()
        	flag = 0

        	if len(line) == 0:
            		print('** class name missing **')
            		return False

        	try:
            		clsname = args[0]
            		eval("{}()".format(clsname))
        	except IndexError:
            		print('** class doesn\'t exist **')
            		return False

        	try:
            		instanceid = args[1]
        	except IndexError:
            		print('** instance id missing **')
            		return False

        	objs = storage.all()
        	try:
            		clschange = objs["{}.{}".format(clsname, instanceid)]
        	except IndexError:
            		print('** no instance found **')
            		return False

        	try:
            		attributename = args[2]
        	except IndexError:
            		print('** attribute name missing **')
            		return False

        	try:
            		updatevalue = args[3]
        	except IndexError:
            		print('** value missing **')
            		return False

       		if updatevalue.isdecimal() is True:
            		setattr(clschange, attributename, int(updatevalue))
            		storage.save()
        	else:
            		try:
                		setattr(clschange, attributename, float(updatevalue))
                		storage.save()
            		except:
                		setattr(clschange, attributename, str(updatevalue))
                		storage.save()

if __name__=='__main__':
	Michezo().cmdloop()
