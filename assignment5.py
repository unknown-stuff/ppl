class BankAccount:
    def __init__(self, account_number, account_holder_name, balance, pin):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        return f"Your account balance is: {self.balance}"

    def withdraw_amount(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. Your updated balance is {self.balance}"
        else:
            return "Insufficient balance."

    def deposit_amount(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. Your updated balance is {self.balance}"
        else:
            return "Invalid deposit amount."

    def mini_statement(self):
        return f"Mini statement: Account Number - {self.account_number}, Balance - {self.balance}"

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN successfully changed."

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def create_account(self):
        account_number = int(input("Enter account number: "))
        if account_number in self.accounts:
            print("Account number already exists. Please use a different account number.")
            return
        account_holder_name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))
        pin = input("Enter pin: ")
        new_account = BankAccount(account_number, account_holder_name, balance, pin)
        self.accounts[account_number] = new_account
        print(f"Account {account_number} successfully created.")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Amount")
        print("3. Deposit Amount")
        print("4. Mini Statement")
        print("5. Change Pin")
        print("6. Create New Account")
        print("7. Quit")

    def perform_operation(self, account_number):
        if account_number not in self.accounts:
            print("Account not found.")
            return
        current_account = self.accounts[account_number]
        while True:
            self.display_menu()
            try:
                choice = int(input("Please enter your choice: "))
                if choice == 1:
                    print(current_account.check_balance())
                elif choice == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    print(current_account.withdraw_amount(amount))
                elif choice == 3:
                    amount = float(input("Enter amount to deposit: "))
                    print(current_account.deposit_amount(amount))
                elif choice == 4:
                    print(current_account.mini_statement())
                elif choice == 5:
                    new_pin = input("Enter new PIN: ")
                    print(current_account.change_pin(new_pin))
                elif choice == 6:
                    self.create_account()
                elif choice == 7:
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid option.")

if __name__ == '__main__':
    atm = ATM()
    account1 = BankAccount(123456789, "John Doe", 5000, '1234')
    account2 = BankAccount(987654321, "Jane Doe", 3000, '5678')
    atm.add_account(account1)
    atm.add_account(account2)
    
    while True:
        print("\n1. Create a new account")
        print("2. Access an existing account")
        print("3. Quit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            atm.create_account()
        elif choice == 2:
            account_number = int(input("Enter your account number: "))
            atm.perform_operation(account_number)
        elif choice == 3:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
