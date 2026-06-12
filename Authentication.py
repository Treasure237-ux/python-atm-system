pin = 1234
balance = 5000
mini_statement = []
def authentication():
    password = int(input("\nEnter your pin: "))
    if password == pin:
        print('Access granted')
        return True
    else:
        print("incorrect password")
        return False


# authentication()