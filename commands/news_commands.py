#!/usr/bin/python3
import sys

""" Command to open files for reading """

def open_news(filename):
	try:
		with open(filename, "r") as news:
			print(news.read())
	except FileNotFoundError:
		print("{} not available".format(filename))
	except Exception as e:
		print("{} encountered".format(e))

if __name__ == "__main__" :
	if len(sys.argv) != 2:
		print("Provide a single filename")
	else:
		filename=sys.argv[1]
		open_news(filename)

