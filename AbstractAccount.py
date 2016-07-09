from abc import ABCMeta, abstractmethod
from InsufficientFundException import InsufficientFundException

class AbstractAccount:
    __metaclass__=ABCMeta
    amount=0
    checkAvbl=False
    roi=0

    def setAmount(self, amount):
       self.amount = amount
       print("Initial Amount deposited in Account")

    def getAmount(self):
        return self.amount;

    def setCheckAvbl(self):
        self.checkAvbl = True

    def getCheckStatus(self):
        return self.checkAvbl

    @abstractmethod
    def setRoi(self):
        pass

    @abstractmethod
    def accountType(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

    def depositAmount(self, amount):
        self.amount = self.amount + amount

    def withdrawAmount(self, amount):
        if self.amount < amount:
            raise InsufficientFundException(self.amount, amount)
        else:
            self.amount = self.amount - amount
            self.getAmount()


