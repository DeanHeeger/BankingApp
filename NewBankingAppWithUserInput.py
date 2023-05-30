class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")
        print(f"New balance: R{self.balance}")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful.")
            print(f"New balance: R{self.balance}")
        else:
            print("Insufficient funds.")


    def display(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: R{self.balance}")


def createAccount():
    print("Enter account holder name: ")
    name = input()
    print("Enter initial balance (optional): ")
    balance = float(input() or 0)

    account = Account(name, balance)

    #Write account data to text file.
    with open('accounts.txt', 'a') as f:
        f.write(f"{account.name}, {account.balance}\n")

    return account

def main():
    accounts = []
    while True:
        print("\n===============================WELCOME TO THE OFFICE HEROES BANKING APP!===============================")
        print("1. Create an account")
        print("2. View account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        print("=========================================================================================================")
        

        user_choice = int(input("Enter choice: "))


        if user_choice == 1:
            account = createAccount()
            accounts.append(account)
            print("Account created successfully.")


        elif user_choice == 2:
            name = input("Enter account holder name: ")
            for account in accounts:
                if account.name == name:
                    account.display()
                    break
                else:
                    print("Account not found!")


        elif user_choice == 3:
            name = input("Enter account holder name: ")
            for account in accounts:
                if account.name == name:
                    amount = float(input("Enter Amount to deposit: R"))
                    account.deposit(amount)
                    break
                else:
                    print("Account not found!")


        elif user_choice == 4:
            name = input("Enter account holder name: ")
            for account in accounts:
                if account.name == name:
                    amount = float(input("Enter amount to withdraw: R"))
                    account.withdraw(amount)
                    break


        elif user_choice == 5:
            print("Thank you for banking with us! See you soon!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()






        





            
