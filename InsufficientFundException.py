class InsufficientFundException(object):
    def __init__(self, availableAmount,withdrawAmount):
        print ("Insufficent fund in your account; you are trying to withdraw " +withdrawAmount + " however you have " + availableAmount + " hence falling short of " + (withdrawAmount-availableAmount))
