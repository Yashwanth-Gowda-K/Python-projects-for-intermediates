class BankAccount:
    def __init__(self, account_number, name , balance =0) :
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposite(self, amount):
        if amount>0:
            self.balance +=amount
            print(f"Successfully deposited {amount}. New balance: {self.balance}")
        else:
            print("Depositve amount must be postive.")

    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully withdraw {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive.")

    def display_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: ₹{self.balance}\n")

class Bank:
    def __init__(self):
        self.accounts = {}
    def create_amount(self, account_number, name,initial_balance= 0):

        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number , name , initial_balance)
            print("Account successfully created!")
        else:
            print("Account with this number already exists.")

    def get_account(self, account_number):
        """
        Retrieve an account object using its account number.
        """
        return self.accounts.get(account_number, None)


# Main program to interact with the bank system
def main():
    """
    Main function to handle user interaction with the bank system.
    """
    bank = Bank()

    while True:
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            # Create a new account
            acc_num = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            try:
                initial_balance = float(input("Enter initial deposit amount (₹): "))
            except ValueError:
                print("Invalid amount! Setting initial balance to ₹0.")
                initial_balance = 0
            bank.create_account(acc_num, name, initial_balance)

        elif choice == 2:
            # Deposit money
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter amount to deposit (₹): "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
            else:
                print("Account not found.")

        elif choice == 3:
            # Withdraw money
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter amount to withdraw (₹): "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
            else:
                print("Account not found.")

        elif choice == 4:
            # View account details
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                account.display_details()
            else:
                print("Account not found.")

        elif choice == 5:
            # Exit the system
            print("Thank you for using the Bank Management System!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


# Run the main function if the script is executed
if __name__ == "__main__":
    main()

    
    

