import os
import time
import random

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
		account_dict = {}
		if not os.path.exists("accounts.txt"):
			return None
		with open("accounts.txt", "r") as f:
			for line in f:
				line = line.strip()
				if not line:
					continue
				parts = line.split(",")
				if len(parts) < 3:
					continue
				name = parts[0]
				pwd = parts[1]
				acct = parts[2]
				bal = parts[3] if len(parts) > 3 else "0"
				account_dict[acct] = {"name": name, "password": pwd, "balance": int(bal)}
		if account_number not in account_dict:
			raise IncorrectAccountNumberError("Incorrect account number")
		if password != account_dict[account_number]["password"]:
			raise IncorrectPasswordError("Incorrect password")
		self.name = account_dict[account_number]["name"]
		self.password = password
		self.account_number = account_number
		self.balance = account_dict[account_number]["balance"]
		return self.name

	def _update_account_in_file(self):
		lines = []
		if os.path.exists("accounts.txt"):
			with open("accounts.txt", "r") as f:
				lines = f.readlines()
		new_lines = []
		for line in lines:
			line = line.strip()
			if not line:
				continue
			parts = line.split(",")
			if len(parts) < 3:
				new_lines.append(line)
				continue
			acct = parts[2]
			if acct == self.account_number:
				new_lines.append(f"{self.name},{self.password},{self.account_number},{self.balance}")
			else:
				if len(parts) > 3:
					new_lines.append(f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}")
				else:
					new_lines.append(line)
		with open("accounts.txt", "w") as f:
			for l in new_lines:
				f.write(l + "\n")

	def withdraw(self, amount, password, account_number):
		data = self.required_checking(password, account_number)
		if amount > self.balance:
			raise BalanceNotEnoughError("Balance not enough")
		self.balance -= amount
		self._update_account_in_file()
		print(f"Withdrawn successfully. Your new balance is {self.balance}")
    
	def input_checking(self, amount):
		if amount < 0:
			raise NegativeAmountError("Amount must be positive")
		self.balance += amount
		if getattr(self, "account_number", None):
			self._update_account_in_file()
		return self.balance
    
	def check_balance(self, password, account_number):
		self.required_checking(password, account_number)
		print(f"Your balance is {self.balance}")
        
	def top_up(self, amount, password, account_number):
		self.required_checking(password, account_number)
		if amount < 0:
			raise NegativeAmountError("Amount must be positive")
		self.balance += amount
		self._update_account_in_file()
		print(f"Top-up successful. Your new balance is {self.balance}")

	def create_account(self, name, password):
		existing = set()
		if os.path.exists("accounts.txt"):
			with open("accounts.txt", "r") as f:
				for line in f:
					parts = line.strip().split(",")
					if len(parts) >= 3:
						existing.add(parts[2])
		acct = None
		for _ in range(1000):
			candidate = "".join(str(random.randint(0, 9)) for _ in range(10))
			if candidate not in existing:
				acct = candidate
				break
		if acct is None:
			raise Exception("Unable to generate unique account number")
		self.name = name
		self.password = password
		self.balance = 0
		self.account_number = acct
		with open("accounts.txt", "a") as f:
			f.write(f"{self.name},{self.password},{self.account_number},{self.balance}\n")
		print(f"Account created successfully. Your account number is {self.account_number}")
bank = Bank("", 0, "", "")
    
def main():
	print("system initializing...")
	print("file checking...")
	path = "accounts.txt"
	if os.path.exists(path):
		print("file found")
	else:
		print("file not found, creating file...")
		with open(path, "w") as f:
			# create an empty accounts file (no sample text)
			f.write("")
		print("file created successfully")

	time.sleep(2)
	print("Welcome to the bank!")
	# Endless menu loop until user chooses to exit
	while True:
		print("What do you want to do?")
		print("1. Check balance")
		print("2. Withdraw")
		print("3. Top up")
		print("4. Create new account")
		print("5. Exit")
		choice = input("Enter your choice (1-5): ")
		try:
			if choice == "1":
				acct = input("Enter account number: ")
				pwd = input("Enter password: ")
				bank.check_balance(pwd, acct)
			elif choice == "2":
				amt_str = input("Enter withdrawal amount: ")
				if not amt_str.isdigit():
					print("Amount must be a positive integer")
					continue
				amount = int(amt_str)
				acct = input("Enter account number: ")
				pwd = input("Enter password: ")
				bank.withdraw(amount, pwd, acct)
			elif choice == "3":
				amt_str = input("Enter top-up amount: ")
				if not amt_str.isdigit():
					print("Amount must be a positive integer")
					continue
				amount = int(amt_str)
				acct = input("Enter account number: ")
				pwd = input("Enter password: ")
				bank.top_up(amount, pwd, acct)
			elif choice == "4":
				name = input("Enter your name: ")
				password = input("Enter your password: ")
				bank.create_account(name, password)
			elif choice == "5":
				print("Exiting...")
				break
			else:
				print("Invalid choice, please select 1-5")
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
