import random

lst=["1","2","3","4","5","6"]
while(True):
    print("\nEnter 0 to roll the dice")
    print("Enter 1 to stop the program")
    choice=input()
    if(choice=="0"):
        roll=random.choice(lst)
        print(f"\n{roll}")
    elif(choice=="1"):
        break
    else:
        print("Invalid Input")

print ("Program Terminated")
