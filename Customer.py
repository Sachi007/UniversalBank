import CheckingAccount
import SavingAccount
import AbstractAccount


class Customer(object):
    name = ""
    age = 0
    address = ""
    account = AbstractAccount.AbstractAccount()

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("Welcome " + self.name + "!!")
        print("Welcome to Universal Bank of India")
        print("you are a new customer account yet to be opened")

    def openSavingAccount(self, amount):
        self.accountType = "Saving"
        self.account = SavingAccount.SavingAccount(amount)

    def openCheckingAccount(self, amount):
        self.accountType = "Checking"
        self.account = CheckingAccount.CheckingAccount()
        self.account.setAmount(amount)

    def getInterest(self):
        self.account.calculateInterest()

    def depositAmount(self, amount):
        self.account.depositAmount(amount)

    def withdrawAmount(self, amount):
        self.account.withdrawAmount(amount)
    def getAccount(self):
        return self.account