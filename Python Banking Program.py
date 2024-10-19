# Python Banking Program

def show_balance(balance):
    print(f"Your current balance is: {balance:.2f}")

def deposit_money(balance):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount < 0:
            print("Invalid deposit amount.")
        else:
            balance += amount
            print(f"Deposit successful. New balance: {balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance

def withdraw_money(balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance:.2f}")
            if balance <= 0:
                print("Warning: Your balance is low.")
        else:
            print("Insufficient funds or invalid amount.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance

def transfer_money(balance):
    try:
        amount = float(input("Enter the amount to transfer: "))
        if amount > 0 and amount <= balance:
            destination_account = input("Enter the destination account number: ")
            if destination_account.isdigit():
                balance -= amount
                print(f"Transfer successful. Remaining balance: {balance:.2f}")
                print(f"Money transferred to account {destination_account}.")
            else:
                print("Invalid destination account number.")
        else:
            print("Insufficient funds or invalid amount.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*************************************")
        print("Welcome to Mazinger Banking System!")
        print("*************************************")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Exit")
        print("-------------------------------------")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                balance = deposit_money(balance)
            elif choice == 3:
                balance = withdraw_money(balance)
            elif choice == 4:
                balance = transfer_money(balance)
            elif choice == 5:
                is_running = False
                print("************************************************")
                print("Thank you for using the Mazinger Banking System!")
                print("************************************************")
            else:
                print("*********************************")
                print("Invalid choice. Please try again.")
                print("*********************************")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()