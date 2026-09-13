print("Check Your Security Code")
security_code =int(input("Enter a security code :"))
if security_code == 5566:
    print("Move To Conditiin 2")
    Department_name = input("Enter Department Name")
    if Department_name == "Finance":
        print("Move to Condition 3")
        Access_level = int(input("Enter a Access level "))
        if Access_level >= 5:
            print("Acess Granted: Welcome to meeting room")
        else:
            print("Insufficient Acess level")
    else:
        print("Acess denied: Department not allowed and Try again")
else:
    print("Invalid Security Code")