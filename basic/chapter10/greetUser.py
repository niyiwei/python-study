import json

fileName = 'userName.json'

with open(fileName, "r") as fObj:
	userName = json.load(fObj)
	print("Welcome back, " + userName + "!")