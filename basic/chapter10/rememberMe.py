import json

# userName = input("What is your name? ")


# with open(fileName, 'w') as fObj:
# 	json.dump(userName, fObj);
# 	print("We'll remeber you when you come back, "+ userName +"!")

def getStoredUserName():
	fileName = "userName.json"
	try:
		with open(fileName, "r") as fObj:
			userName = json.load(fObj)
	except FileNotFoundError:
		return None
	else:
		return userName

def greetUser():
	userName = getStoredUserName();
	if userName:
		print("Welcome back, " + userName + "!")
	else:
		userName = input("What is your name? ")
		with open(fileName, 'w') as fObj:
			json.dump(userName, fObj);
		print("We'll remeber you when you come back, "+ userName +"!")
greetUser()
