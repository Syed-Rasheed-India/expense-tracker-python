
expense_list ={}

def add_expenses():
    month = input("Enter the Month : ")
    expense_title = input("Enter the Expense Title : ")
    expense_amount = int(input("Enter the Expense Amount : "))

    if month not in expense_list:
        expense_list[month] = []
        expense_list[month].append({expense_title: expense_amount})
    else:
        expense_list[month].append({expense_title: expense_amount})


def view_expenses():
    month = input("Enter the Month : ")
    month_list = expense_list[month]
    for expense in month_list:
        for key, value in expense.items():
            print(f"{key} : {value}")


def calculate_monthly_expenses():
    month = input("Enter the Month :")
    month_list = expense_list[month]
    sum=0
    for expense in month_list:
        for key, value in expense.items():
            sum+=value
    print(f"{month} : {sum}")

def exit_option():
    exit()

while True:

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Calculate Monthly Expense")

    option = int(input("Enter your Option : "))

    if option == 1:
        add_expenses()
    elif option == 2:
        view_expenses()
    elif option == 3:
        calculate_monthly_expenses()
    elif option == 4:
        exit_option()
    else:
        print("Invalid Option")





