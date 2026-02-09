# Smart ATM System
correct_pin = "1234"
balance = 5000

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is: $" + str(balance))
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print("Withdrawn: $" + str(amount))
            print("Remaining balance: $" + str(balance))
    elif choice == "3":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited: $" + str(amount))
        print("New balance: $" + str(balance))
    elif choice == "4":
        print("Goodbye")
    else:
        print("Invalid option")
else:
    print("Incorrect PIN")
