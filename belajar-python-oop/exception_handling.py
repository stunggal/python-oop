# class Bank():
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         self.balance -= amount
#         return self.balance
    
#     def input_checking(self, amount):
#         if amount < 0:
#             raise NameError("Amount must be positive")
#         self.balance += amount
#         return self.balance
    
# bank = Bank("John Doe", 1000)
# try:
#     print(bank.withdraw(1500))
# except ValueError as e:
#     print(e)
# try:    
#     print(bank.input_checking(-500))
# except NameError as e:
#     print(e)
    
    

# class BalanceNotEnoughError(Exception):
#     pass

# class NegativeAmountError(Exception):
#     pass
        
# class IncorrectPasswordError(Exception):
#     pass
        
# class IncorrectAccountNumberError(Exception):
#     pass

# class Bank():
#     def __init__(self, name, balance, password, account_number):
#         self.name = name
#         self.balance = balance
#         self.password = password
#         self.account_number = account_number

#     def withdraw(self, amount, password, account_number):
#         if password != self.password:
#             raise IncorrectPasswordError("Incorrect password")
#         if account_number != self.account_number:
#             raise IncorrectAccountNumberError("Incorrect account number")
#         if amount > self.balance:
#             raise BalanceNotEnoughError("Insufficient funds")
#         self.balance -= amount
#         print(f"Withdrawn successfully. Your new balance is {self.balance}")
    
#     def input_checking(self, amount):
#         if amount < 0:
#             raise NegativeAmountError("Amount must be positive")
#         self.balance += amount
#         return self.balance
    
#     def check_balance(self, password, account_number):
#         if password != self.password:
#             raise IncorrectPasswordError("Incorrect password")
#         if account_number != self.account_number:
#             raise IncorrectAccountNumberError("Incorrect account number")
#         print(f"Your balance is {self.balance}")
        
#     def top_up(self, amount, password, account_number):
#         if amount < 0:
#             raise NegativeAmountError("Amount must be positive")
#         if password != self.password:
#             raise IncorrectPasswordError("Incorrect password")
#         if account_number != self.account_number:
#             raise IncorrectAccountNumberError("Incorrect account number")
#         self.balance += amount
#         print(f"Top-up successful. Your new balance is {self.balance}")
    
# bank = Bank("John Doe", 1000, "password123", "1234567890")

# try:    
#     Bank.withdraw(bank, 1500, "password123", "1234567890")
#     Bank.check_balance(bank, "password123", "1234567890")
#     Bank.top_up(bank, 500, "password123", "1234567890")
# except BalanceNotEnoughError as e:
#     print(e)
# except IncorrectPasswordError as e:
#     print(e)
# except IncorrectAccountNumberError as e:
#     print(e)
    
# try:    
#     Bank.check_balance(bank, "password123", "1234567890")
#     Bank.top_up(bank, 500, "password123", "1234567890")
#     Bank.withdraw(bank, 1500, "password123", "1234567890")
# except BalanceNotEnoughError as e:
#     print(e)
# except IncorrectPasswordError as e:
#     print(e)
# except IncorrectAccountNumberError as e:
#     print(e)


class BalanceNotEnoughError(Exception):
    pass

class NegativeAmountError(Exception):
    pass
        
class IncorrectPasswordError(Exception):
    pass
        
class IncorrectAccountNumberError(Exception):
    pass

class Bank():
    def __init__(self, name, balance, password, account_number):
        self.name = name
        self.balance = balance
        self.password = password
        self.account_number = account_number
        
    def required_checking(self, password, account_number):
        if password != self.password:
            raise IncorrectPasswordError("Incorrect password")
        if account_number != self.account_number:
            raise IncorrectAccountNumberError("Incorrect account number")

    def withdraw(self, amount, password, account_number):
        self.required_checking(password, account_number)
        if amount > self.balance:
            raise BalanceNotEnoughError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrawn successfully. Your new balance is {self.balance}")
    
    def input_checking(self, amount):
        if amount < 0:
            raise NegativeAmountError("Amount must be positive")
        self.balance += amount
        return self.balance
    
    def check_balance(self, password, account_number):
        self.required_checking(password, account_number)
        print(f"Your balance is {self.balance}")
        
    def top_up(self, amount, password, account_number):
        self.required_checking(password, account_number)
        if amount < 0:
            raise NegativeAmountError("Amount must be positive")
        self.balance += amount
        print(f"Top-up successful. Your new balance is {self.balance}")
    
bank = Bank("John Doe", 1000, "password123", "1234567890")

try:    
    Bank.withdraw(bank, 1500, "password123", "1234567890")
    Bank.check_balance(bank, "password123", "1234567890")
    Bank.top_up(bank, 500, "password123", "1234567890")
except BalanceNotEnoughError as e:
    print(e)
except IncorrectPasswordError as e:
    print(e)
except IncorrectAccountNumberError as e:
    print(e)
    
try:    
    Bank.check_balance(bank, "password123", "1234567890")
    Bank.top_up(bank, 500, "password123", "1234567890")
    Bank.withdraw(bank, 1500, "password123", "1234567890")
except BalanceNotEnoughError as e:
    print(e)
except IncorrectPasswordError as e:
    print(e)
except IncorrectAccountNumberError as e:
    print(e)