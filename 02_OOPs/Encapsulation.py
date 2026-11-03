class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,new_balance):
        if new_balance<0:
            print("Alert: Negative balance denied!")
            self.__balance=0
        elif new_balance>1000000:
            print("Alert: Exceeds FDIC insurance limit! and balance is set to 1000000")
            self.__balance=1000000
        else:
            self.__balance=new_balance

account1=BankAccount(-90)
print(account1.balance)
account1=BankAccount(1000000000000000000)
print(account1.balance)
account1=BankAccount(300)
print(account1.balance)
