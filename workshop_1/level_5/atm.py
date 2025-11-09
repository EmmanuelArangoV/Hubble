accounts = {
    "1234567890": {"password": "1234", "balance": 500000.0, "transactions": []},
    "0987654321": {"password": "0000", "balance": 2200000.0, "transactions": []},
    "2468013579": {"password": "0000", "balance": 453800.0, "transactions": []},
    "6575474849": {"password": "0000", "balance": 987650.0, "transactions": []}
}

atm_money = 1000000

menu = (""
        "1. Check your balance.\n"
        "2. Withdraw your money.\n"
        "3. Consult your transactions.\n"
        "4. Exit\n")

while True:
    print("Welcome to Riwi ATM")
    option = input(menu)

    if option == "1":
        suboption = input("Enter your bank account: ")
        if suboption in accounts:
            password = input("Enter your password: ")
            real_password = accounts[suboption]["password"]
            if password == real_password:
                balance = accounts[suboption]["balance"]
                print(f"Your balance is: {balance}")
            else:
                print("Invalid password.")
        else:
            print("This account does not exist.")
    elif option == "2":
        suboption = input("Enter your bank account: ")
        if suboption in accounts:
            password = input("Enter your password: ")
            real_password = accounts[suboption]["password"]
            if password == real_password:
                print("Remember you can only withdraw the 50% of your total balance.")
                available_money = accounts[suboption]["balance"] * 0.5
                print(f"You can try to withdraw {available_money}.")
                try:
                    money = float(input("How much money would you like to withdraw? "))
                    if money <= available_money:
                        if money <= atm_money:
                            accounts[suboption]["balance"] -= money
                            atm_money -= money
                            accounts[suboption]["transactions"].append(money)
                            print("Please withdraw your money. Keep it safe")
                        else:
                            print("We're sorry the ATM machine doesn't have enough money.")
                    else:
                        print("You can't withdraw that amount of money.")
                except ValueError:
                    print("That is not a valid number.")
            else:
                print("Invalid password.")
        else:
            print("This account does not exist.")
    elif option == "3":
        suboption = input("Enter your bank account: ")
        if suboption in accounts:
            password = input("Enter your password: ")
            real_password = accounts[suboption]["password"]
            if password == real_password:
                print("Your transactions are:")
                for i, transaction in enumerate(accounts[suboption]["transactions"], start = 1):
                    print(f"Transaction {i}: ${transaction}")
            else:
                print("Invalid password.")
        else:
            print("This account does not exist.")
    elif option == "4":
        print("Thanks for using our service.")
        break
    else:
        print("Invalid option.")

# accounts: mapping of account_number to dict with password, balance and transactions list
# atm_money: total cash available in the ATM machine
# menu: user options shown at each prompt
# main loop: keep interacting with user until they choose to exit
    # Option 1: Check balance - verify account exists and password, then display balance
    # Option 2: Withdraw - verify auth, limit withdrawal to 50% of balance, check ATM funds,
    # update account balance and ATM cash, and record transaction
                    # handle invalid numeric input for withdrawal amount
    # Option 3: Consult transactions - verify auth and then list stored transactions
    # Option 4: Exit - thank user and break the loop
    # Invalid option: notify user
