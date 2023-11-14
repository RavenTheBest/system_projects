def check_login(user,pwd):
	if user in data and data[user]["password"] == pwd:
		return True
	else:
		return False
	
def check_validation(user,pwd,confirm_pwd):
	if pwd == confirm_pwd and user not in data:
		data[user] = {"password":pwd}
		return True
	else:
		return False


data = {"user": {"password": "pass"}}

logged = False
username = ""

default_text = """[1] Login
[2] Signup
"""

while True:
	while not logged:
		print(default_text)
		option = input("Choose: ")
		
		if option == "1":
			user = input("Username: ")
			pwd = input("Password: ")
			check = check_login(user,pwd)
			
			if check:
				username, logged = user, True
			else:
				print("Invalid username or password")
		elif option == "2":
			user = input("Username: ")
			pwd = input("Password: ")
			confirm_pwd = input("Confirm password: ")
			valid = check_validation(user,pwd,confirm_pwd)
			if valid:
				username,logged = user, True
				print("Account created succesfully")
			elif user in data:
				print("Username already exist!")
			else:
				print("Password doesnt matched")
			
		else: print("Invalid option")	
	while logged:
		print(f"Hello, {username}!")
		print("[1] Logout\n")
		option = input("Choose: ")
		
		if option == "1": username,logged = "",False
		else: print("Invalid input!")
		
		
