#Stone paper and scissor
import random
def print_choices():
    print("Enter 1 for Stone")
    print("Enter 2 for Scissors")
    print("Enter 3 for Paper")

print("****************Welcome to the Stone/Scissors/Paper Game**************")
print("")
print("****************May the force be with you**************")
print("")
print("****************Begin*******************")
print("")


choice=True
user = 0
computer = 0
while(choice):
    print("")
    print_choices()
    print("")
    inp = int(input("Enter user choice: "))
    print("")
    comp_choice = random.randint(1,3)

    while comp_choice == inp:
        comp_choice = random.randint(1,3)

    if user==5:
        print("")
        print("The winner is user")
        break

    if computer==5:
        print("")
        print("The winner is machine")
        break

    if(inp<1 or inp>3):
        print("")
        print("Please....enter from the given choices!!")
        print("")
        print("")
        continue

    if inp==1 and comp_choice==2:
        print("I choose Stone")
        print("")
        user = user+1
        print("Uggh,lost to the petty human")
        print("")
        print("User: ",user)
        print("")
        print("Computer: ",computer)
        print("")
        print("")
        
    elif inp==2 and comp_choice==3:
        print("I choose Scissors")
        print("")
        user = user+1
        print("Uggh,lost to the petty human")
        print("")
        print("User: ",user)
        print("")
        print("Computer: ",computer)
        print("")
        print("")

    elif inp==3 and comp_choice==1:
        print("I choose paper")
        print("")
        user = user+1
        print("Uggh,lost to the petty human")
        print("")
        print("User: ",user)
        print("")
        print("Computer: ",computer)
        print("")
        print("")

    elif inp==2 and comp_choice==1:
        print("I choose scissors")
        print("")
        computer = computer+1
        print("Machine thrived over the human")
        print("")
        print("User: ",user)
        print("")
        print("Computer: ",computer)
        print("")
        print("")

    elif inp==3 and comp_choice==2:
        print("I choose paper")
        print("")
        computer = computer+1
        print("Machine thrived over the human")
        print("")
        print("User: ",user)
        print("")
        print("Computer: ",computer)
        print("")
        print("")

    elif inp==1 and comp_choice==3:
        print("I choose Stone")
        print("")
        computer = computer+1
        print("Machine thrived over the human")
        print("")
        print("User: ",user)
        print("")
        print("Computer: ",computer)
        print("")
        print("")
    
            
        
        
