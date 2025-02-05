import random

computer = random.choice([1,2,3])
yourInput = input("Enter From Following\n stone \n paper \n scissor \n:")
mainDict = {
    "stone" : 1, 
    "paper" : 2,
    "scissor": 3
}
if yourInput not in mainDict:
    print("You Entered a Wrong String. Please choose stone, paper, or scissor.")
    exit()

else:
    user = mainDict[yourInput]
    ReverseDict = {1 : "stone", 
                   2 : "paper", 
                   3 : "scissor"}  
    print(f"Here You Choose :{ReverseDict[user]}")
    print(f"Computer Choose :{ReverseDict[computer]}") 

#  THIS IS THE SORT LOGIC UNDERSTAND AFTER SHOW FULL PROGRAM
# if(computer - user == -1) or (computer - user == 2):
#     print("🎉Congratulations, You Win")

# else:
#     print("😣Try Again, You are Lost")
        
  

if(computer == 1 and user == 1) or (computer == 2 and user == 2) or (computer == 3 and user == 3):
    print("😵This is Draw")

else:
    if(computer == 1 and user == 2):  #-1 Win
        print("🎉Congratulations, You Win")

    elif(computer == 1 and user == 3):    #-2 lost
        print("😣Try Again, You are Lost")

    elif(computer == 2 and user == 1):      #1 lost
        print("😣Try Again, You are Lost")

    elif(computer == 2 and user == 3):      # -1 Win
        print("🎉Congratulations, You Win")

    elif(computer == 3 and user == 1):      #2 Win
        print("🎉Congratulations, You Win")

    elif(computer == 3 and user == 2):      #1 lost
        print("😣Try Again, You are Lost")

    else:
        print("Something Went Wrong")
