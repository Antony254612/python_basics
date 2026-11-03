#bank acc==owner,acc no,balance,history
class Client:
    def __init__(self,names,kra_pin,dob,gender):
        self.names=names
        self.kra_pin=kra_pin
        self.dob=dob
        self.gender=gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)

class BankAccount:
    def __init__(self,owner,acc_no,balance):
        self.owner=owner
        self.acc_no=acc_no
        self.balance=float(balance)
    def deposit(self,amount):
        self.balance += abs(amount)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)
    def print_details(self):
        print(self.owner)
        print(self.acc_no)
        print(self.balance)
        print("--------------")

#create owners
jane=Client('Jane Mwangi','A09876','1999-01-18','F')
Mike=Client('Mike Julia','A096776','1989-11-28','F')

acc1=BankAccount(jane,acc_no='1111',balance='20000')
acc2=BankAccount(jane,acc_no='12451',balance='2700')
acc3=BankAccount(Mike,acc_no='34567',balance='24500')

acc1.deposit(5000)
acc2.deposit(300)

acc1.print_details()
acc1.withdraw(6000)
acc1.print_details()





