import time

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
  
bank = Bank("BCA", 1000000, "password123", "1234567890")
    
def main():
	print("system initializing...")
	time.sleep(2)
	print("Welcome to the bank!")
	print("What do you want to do?")
	print("1. Check balance")
	print("2. Withdraw")
	print("3. Top up")
	# print("4. Create new account")
	choice = input("Enter your choice (1-3): ")
	try:
		match choice:
			case "1":
				bank.check_balance("password123", "1234567890")
			case "2":
				amount = int(input("Enter withdrawal amount: "))
				bank.withdraw(amount, "password123", "1234567890")
			case "3":
				amount = int(input("Enter top-up amount: "))
				bank.top_up(amount, "password123", "1234567890")
	except BalanceNotEnoughError as e:
		print(e)
	except NegativeAmountError as e:
		print(e)
	except IncorrectPasswordError as e:
		print(e)
	except IncorrectAccountNumberError as e:
		print(e)
main()

print("Thank you for using the bank. Goodbye!")
