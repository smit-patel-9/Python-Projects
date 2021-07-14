import random

list=[]
for i in range (0,101):
    list.append(i)
    
print("+"*60)

def result():
    user = input("Are You Continue (y/n) : ")
    if user == "y" or user == "Y":
        list.remove(LuckyNumber)
        print("+"*60)
        return True
    
    elif user == "n" or user == "N":
        list.remove(LuckyNumber)
        print("\n",list)
        print("+"*60)
        return False
        
    else:
        print("\n!!!!!!!!! Please Enter (y/n) !!!!!!!!!\n")
        return result()

condition = True
while condition:

    LuckyNumber = random.choice(list)
    print("\nLucky Number is : ",LuckyNumber)

    condition = result()
    if condition == False:
        break
    else:
        continue
    
    
            
