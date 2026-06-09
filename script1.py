amount = 0

def balance():
    print("Balance =", amount)

def deposit(amt):
    global amount
    amount += amt

def withdraw(amt):
    global amount
    amount -= amt

while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    try:
        option = int(input("Enter Your Option : "))
    except ValueError:
        print("Please enter a valid option")
        continue

    match option:
        case 1:
            balance()

        case 2:
            try:
                deposit_amount = int(input("Enter Your Deposit Amount : "))
                if deposit_amount > 0:
                    deposit(deposit_amount)
                    print("Deposit Successful")
                else:
                    print("Amount should be greater than 0")
            except ValueError:
                print("Please enter a valid number")

        case 3:
            try:
                withdraw_amount = int(input("Enter Your Withdraw Amount : "))
                if withdraw_amount > 0:
                    withdraw(withdraw_amount)
                    print("Withdraw Successful")
                else:
                    print("Amount should be greater than 0")
            except ValueError:
                print("Please enter a valid number")

        case 4:
            print("Program Ended")
            break

        case _:
            print("Invalid Option")