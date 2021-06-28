def isValid(password):

    if (len(password) < 8 or len(password) == 0):
        print("Password should be more than 8 characters and not be null")
        return False


    if (True):
        count = 0

        # check digits from 0 to 9
        arr = ['0', '1', '2', '3',
               '4', '5', '6', '7', '8', '9']

        for i in password:
            if i in arr:
                count = 1
                break

        if count == 0:
            print("Password should contain one number at least")
            return False


    if True:
        count = 0

        # checking capital letters
        for i in range(65, 91):

            if chr(i) in password:
                count = 1

        if (count == 0):
            print("Password should have one uppercase letter at least")
            return False

    if (True):
        count = 0

        # checking small letters
        for i in range(90, 123):

            if chr(i) in password:
                count = 1

        if (count == 0):
            print("password should have one lowercase letter at least ")
            return False

    # if all conditions fails
    return True


# code
password1 = input("Enter Password: ")

if (isValid([i for i in password1])):
    print("Valid Password")
else:
    print("Invalid Password!!!")