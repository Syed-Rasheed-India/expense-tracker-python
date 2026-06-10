import random

while True:
    print("1. Start")
    print("2. End")
    option = int(input("Enter a Option: "))
    if option == 2:
        break
    else:
        random_number = random.randint(1, 10)
        attempt=0
        while True:
            number = int(input("Enter a Number From 1 to 10: "))
            if number == random_number:
                # global attempt
                print("You Won! you Won by ",attempt,"Attempts")
                break
            elif number > random_number:
                # global attempt
                attempt+=1
                print("your Number is Higher !! Try Again")
            elif number < random_number:
                # global attempt
                attempt+=1
                print("your Number is Lower !! Try Again")




