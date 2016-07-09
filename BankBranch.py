import Customer
class BankBranch(object):

    if __name__=='__main__':
        customer1=Customer.Customer("Sachchidanand", 34, "Greater Noida")
        customer1.openCheckingAccount(5000)
        print("Hi "+customer1.name+"!! \n The Aailable Balance in your account is " + str(customer1.getAccount().getAmount()))