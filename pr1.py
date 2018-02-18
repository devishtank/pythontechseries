numOfTry = 0

while (numOfTry<=3):
	username = raw_input("username? ")
	password = raw_input("password? ")

	if(username == "procodecg" and password == "12345678"):
		numOfTry = 4
		print "You are allowed to enter the system",username
	else:
		print "You are not allowed to enter the system",username
		if(numOfTry >= 3):
			break

		wannaTryAgain = "x"

		while(wannaTryAgain!="y" and wannaTryAgain!="n"):
			wannaTryAgain = raw_input("Do you wanna try again? (y/n) ")
			if(wannaTryAgain == "y"):
				numOfTry = numOfTry + 1
				print "There are ", 3-numOfTry, " try left again"
			elif(wannaTryAgain == "n"):
				numOfTry = 4