print("WelCome To My Networking Basics Quiz")

player = input("Do You Want Play My Quiz? ")
if player.lower() != "yes":
 quit()

print("Let's go") 
score = 0

answer = input("What does MAC stand for? ")
if answer.lower() == "media access control":
 print("Correct!")
 score += 1
else:
 print("Incorrect")


answer = input("What does NIC stand for? ")
if answer.lower() ==("network interface card"):
 print("Correct!")
 score += 1
else:
 print("Incorrect")


answer = input("What does WIFI stand for? ")
if answer.lower() == "wireless fidelity":
 score += 1
 print("Correct!")
else:
 print("Incorrect")


answer = input("What does IP stand for? ")
if answer.lower() == ("internet protocol"):
 score += 1
 print("Correct!")
else:
 print("Incorrect")


answer = input("What does DNS stand for? ")
if answer.lower() == ("domain name system"):
 score += 1
 print("Correct!")
else:
 print("Incorrect") 


answer = input("What does WLAN stand for? ")
if answer.lower() == ("wireless local area network"):
 score += 1
 print("Correct!")
else:
 print("Incorrect")


answer = input("What does FTP stand for? ")
if answer.lower() == ("file transfer protocol"):
 score += 1
 print("Correct!")
else:
 print("Incorrect")


answer = input("What does VPN stand for? ")
if answer.lower() == ("virtual private network"):
 score += 1
 print("Correct!")
else:
 print("Incorrect")


answer = input("What does AP stand for? ")
if answer.lower() == ("access point"):
 score += 1
 print("Correct!")
else:
 print("Incorrect")

answer = input("What does SMTP stand for? ")
if answer.lower() == ("simple mail transfer protocol"):
 score += 1
 print("Correct!")
else:
 print("Incorrect")
print("Your Answer " + str(score) + " Questions!")
print("You Answer " + str((score/10) * 100) + "%")
