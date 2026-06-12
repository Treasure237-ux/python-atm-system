import Authentication as AU
mini_statement = AU.mini_statement
balance = AU.balance
pin = AU.pin


def atm_system():
    global balance, mini_statement, pin 
    while True:
        print("\n\n**********ATM MENU**********")
        print("1: Check balance")
        print("2: Deposit money")
        print("3: withdraw money")
        print("4: change pin")
        print("5: mini statement")
        print("6: Exit system")
        print("*****************************")

        choice = input("Enter a number: ")

        if choice == "1":
            print(f'your balance is {balance}')
            mini_statement.append("checked balanced")
        elif choice == "2":
            amt = float(input("Enter Amount: "))
            if amt > 0:
                balance += amt        
                mini_statement.append(f"Deposited {amt}")
                print(f"current balanece is {balance}")
            else:
                print("invalid amount")
        elif choice == "3":
            amt = float(input("Enter withdrawal amount: "))
            if amt <= balance:
                if amt > 0:
                    balance -= amt
                    print("withdraw successful")
                    print(f"current balance is {balance}")
                    mini_statement.append(f"withdrew {amt}")
                else:
                    print("invalid amount")
            else:
                print("insufficient funds")
        elif choice == "4":
            old_pin = int(input("Enter old pin: "))
            if old_pin == pin:
                new_pin = int(input("Enter new pin: "))
                confirm_pin = int(input("confirm new pin: "))
                if new_pin == confirm_pin and new_pin != pin:
                    pin = new_pin
                    print("pin changed successfully🎊🎊")
                    mini_statement.append("changed pin")
                else:
                    print("pin mismatched or new pin cannot be same as old pin")
            else:
                print("incorrect pin")
        elif choice == "5":
            print("\n**********MINI STATEMENT**********")
            if len(mini_statement) == 0:
                print("No transaction found")
            else:
                for i in mini_statement:
                    print(f"--> {i}")
        elif choice == "6":
            print("\nThank you for transacting with us 🎊😊😊\n\n")
            break
        else:
            print("invalid option")




if AU.authentication():
    atm_system()
else:
    print("Access denied😪😪")
