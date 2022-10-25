class BankAccount:

# constructor
    def __init__(self):
        print (f"constructor from BankAccount{self}")
    def __del__(self):
        print (f"destructor from BankAccount{self}")

# class BankAccount():
#     pass
#
# class BankAccount(object):
#     pass



account1 = BankAccount()
print (account1)
#BankAccount.__init__(account1)
#account1.name = "12345"
#account1.balance = 1_000_000

account2 = BankAccount()
print(account2)
#account2.name = "67890"
#account2.balance = 1_000

#account3 == account2