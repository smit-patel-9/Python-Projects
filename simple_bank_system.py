class Bank:

    def __init__(self):
        try:
            bal=open("balance.txt","r")
            data=bal.read().split( )
            d=data[0]
            self.balance=int(d)
            bal.close()
        except:
            bal=open("balance.txt","w")
            bal.close()
        
    
    def AccountOpen(self,name,balance):
        self.name=name
        self.balance=balance
 
        print(self.name,"Your Account Successfully Created.")
        print("Initial Blance is",self.balance,"Rs.")

    def Deposit(self,amount):
        self.balance=self.balance+amount

    def WithDraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print(amount,"Balance not available")

    def CheckBalance(self):
        bal=open("balance.txt","w")
        bal.write(str(self.balance))
        bal.close()
        print("Current Balance is : ",self.balance)
        return self.balance

    def Statement(self):
        file = open("BankStatement.txt","r+")
        print(file.read())

user = Bank()

name = input("Please Enter Your Name : ")
try:
    file = open("BankStatement.txt","r")
except:
    file = open("BankStatement.txt","w+")

    balance = int(input("Please Enter Initial Balance : "))
    if balance == None:
        user.AccountOpen(name)
    else:
        user.AccountOpen(name,balance)
    file.write("\nAccount Opening Balance Is : "+str(balance)+"Rs.")

finally:
    file.close()

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Statement")
    print("5. exit\n")

    n = int(input("Enter The Number : "))

    if n == 1:
        amount=int(input("Enter The Amount : "))
        user.Deposit(amount)
        file = open("BankStatement.txt","a")
        file.write("\nDeposit : "+str(amount)+"Rs.")
        file.close()
        
    elif n == 2:
        amount=int(input("Enter The Amount : "))
        user.WithDraw(amount)
        file = open("BankStatement.txt","a")
        file.write("\nWithDraw : "+str(amount) +"Rs.")
        file.close()
       
    elif n == 3:
        user.CheckBalance()
        
    elif n == 4:
        user.Statement()
        
    elif n == 5:
        
        break
    
    else:
        print("Please Enter valid Number")

