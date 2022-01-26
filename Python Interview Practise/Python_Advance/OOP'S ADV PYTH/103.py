# Banking application demo
from queue import PriorityQueue


class customer:
    def __init__(self,amount,balance=0.0):
        self.amoount=amount;
        self.balance=balance;
    def deposit(self,amount):
         self.balance=self.balance+amount
         print("The balance is:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds")
        else:
            print("The amount withdrawn is: ",amount, "and remaining balance is:",self.balance-amount)

#c1=customer()
name=input("Enter the name: \n")
c1=customer(name)
while True:
     print("Required operation to be carried out::\n Withdraw-w,Deposit-d,exit-e")
     option=input("Enter the operation ")
     if option.lower()=='w':
         print("Enter the required amt to withdraw:\n")
         amt=float(input())
         c1.withdraw(amt)
     elif option.lower()=='d':
         print("Enter the required amt to deposit:\n")
         amt1=float(input())
         c1.deposit(amt1)
     elif option.lower()=='e':
         print("Thankyou for using the service:")
         break
     else:
         print("Enter the desired info to carried out")





