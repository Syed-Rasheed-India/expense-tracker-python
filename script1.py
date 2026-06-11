while True:

    password = input("Enter Strong Password:")
    captial =0
    digit=0
    special =0

    if len(password) < 8:
        print("Password is too short")
        break

    for i in password:

        if i.isupper():
            captial += 1

        if i.isdigit():
            digit += 1

        if not i.isalnum():
            special+=1

    if captial==0:
        print("must be 1 or more capital letters")
        break

    if digit==0:
        print("must be 1 or more digit letters")
        break

    if  special ==0:
        print("must be 1 or more special letters")
        break

    if captial>=1 and digit>=1 and special >=1:
        print("password is too long")
        break



