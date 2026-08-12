balance = 10000
print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Choose an option: "))
if choice == 1: 
    print("Balance:" , balance)
elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("New Balance:" , balance)
elif choice ==3:
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance = balance - amount
        print("New Balance: ", balance)
    else:
        print("Insufficient Balance")
elif choice == 4:
        print("Thanks you for using our ATM!")

else:
     print("Invalid Choice")



