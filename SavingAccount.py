from AbstractAccount import AbstractAccount
import math


class SavingAccount(AbstractAccount):
    def __init__(self,amount,roi):
        self.amount=amount
        self.roi=roi
        print("Welcome to Universal Bank of India")
        print ("Saving Account Opened")
    def setRoi(self,roi):
        self.roi=roi
    def getAccountType(self):
        return "Saving"
    def calculateInterest(self,time):
        interest= self.amount*math.pow[(1+self.roi/100),time]
        return interest
    def updateInterest(self, time):
        interest=self.calculateInterest(time)
        self.amount+=interest