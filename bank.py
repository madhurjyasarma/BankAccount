class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def acc_owner(self):
        print(f"Account owner: {self.owner}")
    def acc_balance(self):
        print(f"Account balance: {self.balance}")

    def deposit(self,add_balance):
        self.balance = self.balance + add_balance
        print(f"Amount of {add_balance} is deposited in your account")
        print(f"Total Amount is : {self.balance}")

    def withdraw(self,deduct_money):

        if deduct_money > self.balance:
            print("Funds Unavailable")
        else:
            self.balance = self.balance - deduct_money
            print(f"Amount of {deduct_money} is withdrawn from your account")
            print(f"Total Amount is : {self.balance}")

my_account = Account("Madhurjya",100)


my_account.acc_owner()
my_account.acc_balance()

my_account.withdraw(500)
# print(my_account.owner)
# print(my_account.balance)
