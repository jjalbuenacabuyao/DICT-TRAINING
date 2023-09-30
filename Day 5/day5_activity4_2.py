from day5_activity4 import BankAccount

# joel_bank_account = BankAccount("Joel Cabuyao", 100)
# joel_bank_account.deposit(1000)
# joel_bank_account.withdraw(100)
# joel_bank_account.check_balance()

# test_bank_account = BankAccount("John", 500)
# test_bank_account.deposit(500)
# test_bank_account.withdraw(1000)
# test_bank_account.check_balance()

accounts: list[BankAccount] = []

while True:
    print("""
Joel's Bank Commands:
    1 - Deposit
    2 - Withdraw
    3 - Check balance
    4 - Create a bank account
    5 - Exit
""")
    command = input("Enter command: ")

    if command == "1":
        name = input("Enter account holder name: ").title()
        account_does_not_exist = False

        for account in accounts:
            if account.account_holder == name:
                amount_to_be_deposited = float(input("Enter the amount you want to deposit: "))
                account.deposit(amount_to_be_deposited)
                account_does_not_exist = False
                break

            else:
                account_does_not_exist = True

        
        if account_does_not_exist:
            print("Account does not exist.")
                
    elif command == "2":
        name = input("Enter account holder name: ").title()
        account_does_not_exist = False

        for account in accounts:
            if account.account_holder == name:
                amount_to_be_withdrawn = float(input("Enter the amount you want to deposit: "))
                account.withdraw(amount_to_be_withdrawn)
                account_does_not_exist = False
                break

            else:
                account_does_not_exist = True

        
        if account_does_not_exist:
            print("Account does not exist.")

    elif command == "3":
        name = input("Enter account holder name: ").title()
        account_does_not_exist = False

        for account in accounts:
            if account.account_holder == name:
                account.check_balance()
                account_does_not_exist = False
                break

            else:
                account_does_not_exist = True

        
        if account_does_not_exist:
            print("Account does not exist.")

    elif command == "4":
        name = input("Enter account holder name: ").title()

        new_account = BankAccount(name, 0)
        accounts.append(new_account)
        print("Account created successfully.")

    elif command == "5":
        print("Terminating program....")
        break

    else:
        print("Invalid command.")

        