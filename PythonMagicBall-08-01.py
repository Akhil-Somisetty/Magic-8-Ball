#importing Modules
import sys
import random
#initialize Variables
response = ["IT IS CERTAIN","YOU MAY RELY ON IT","AS I SEE IT, YES","OUTLOOK LOOKS GOOD","MOST LIKELY","IT IS DECIDELY SO","WITHOUT A DOUBT","YES, DEFINETLY"]
check = True
#Condition
while check :
    question = input("Please Ask the Magic 8 ball a Question?")
    if len(question) == 0:
        break
    print(random.choice(response))
