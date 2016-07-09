from AbstractAccount import AbstractAccount


class CheckingAccount(AbstractAccount):
    def __init__(self):
        print("Welcome to Universal Bank of India")
        print ("default Account Opened")
    def setRoi(self,roi):
        self.Roi=roi
    def setAccountType(self):
        return "Checking"

    def calculateInterest(self, time):
        interest = self.amount *self.roi*time/100
        return interest

    def updateInterest(self, time):
        interest = self.calculateInterest(time)
        self.amount += interest