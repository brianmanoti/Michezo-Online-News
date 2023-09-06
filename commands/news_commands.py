#!/usr/bin/env bash
import sys
""" Command to open file """

def open_news(filename):
	try:
		with open("filename", "r") as news:
			print(news.read())
	except FileNotFoundError:
		print("{} not found".format(filename))
	except Exception:
		print("An {} occured".format(Exception))

if __name__=="__main__":
	if len(sys.argv) !=2:
		print("Add a filename after script command")
	else:
		filename = sys.argv[1]
		open_news(filename)

	
