#Individual customer information
customerInformation1 = {
    "PIN" : 1234,
    "name" : "Gurpreet Kaur",
    "attempts" : 0,
    "status" : "active",
    "balance" : 4000 
}
customerInformation2 = {
    "PIN" : 5678,
    "name" : "Sean Greaves",
    "attempts" : 0,
    "status" : "active",
    "balance"  : 20635.15 
}
customerInformation3 = {
    "PIN" : 9876,
    "name" : "Ashley Greaves",
    "attempts" : 0,
    "status" : "active",
    "balance"  : 45236.25 
}
#Dictonary of customers information
customersInformation = {
    1 : customerInformation1,
    2 : customerInformation2,
    3 : customerInformation3
}
#Displaying the menu
def displayMenu():
    try:
        userInput = int(input(f"Please select one (1/2/3/4)\n\
                            1. Display the balance?\n\
                            2. Withdraw Money?\n\
                            3. Make a Deposit?\n\
                            4. Exit?\n"))
        if userInput not in [1,2,3,4]:
            print("Invalid choice. Please select a valid option.")
        return userInput
    except ValueError:
        print("Invalid input. Please enter a number.")

#Withdrawing amount from an account balance
def withdrawal(balance):
    try:
        userInput = int(input(f"Please select the withdrawal amount (1/2/3/4/5/6)\n\
                          1. $20\n\
                          2. $40\n\
                          3. $60\n\
                          4. $80\n\
                          5. $100\n\
                          6. Other\n"))
        if userInput not in [1,2,3,4,5,6]:
            print("Invalid choice. Please select a valid option.")
        #Setting the withdraw amount
        if (userInput == 1):
            withdraw = 20
        if (userInput == 2):
            withdraw = 40
        if (userInput == 3):
            withdraw = 60
        if (userInput == 4):
            withdraw = 80
        if (userInput == 5):
            withdraw = 100
        if (userInput == 6):
            customAmount = float(input("Enter the amount to withdraw: "))
            withdraw = customAmount
        #Checking if the balance is more than the withdraw amount
        if(balance > withdraw):
            balance = balance - withdraw
            print(f"Your new balance is ${'{:.2f}'.format(balance)}")
            return balance
        else:
            print(f"Balance lower than ${withdraw}. Try again with another amount.")
    except ValueError:
        print("Invalid input. Please enter a number.")
#Depositing amount into the account balance
def deposit(balance):
    try:
        balance += float(input("Enter the amount to deposit in the account: "))
        print(f"Your new balance is ${'{:.2f}'.format(balance)}")
        return balance
    except ValueError:
        print("Invalid input. Please enter a number.")
#exit program
def exitingProgram():
    print("Exiting program... Thank you!")
    exit()


#Print welcome message
print("Welcome to Humber bank terminal!!")
try: 
    enteredAccount = int(input("Please enter your account number: "))
    #Check if the account number exists
    if enteredAccount in customersInformation:
        currentCustomer = customersInformation[enteredAccount]
        currentCustomerId = enteredAccount
        for i in range(3):
            try:
                enteredPIN = int(input("Enter 4-digit PIN: "))
            except ValueError:
                print("Invalid input. Please enter a 4-digit PIN.")
            #Match the PIN of the customer in the dictonary
            if(currentCustomer["PIN"] == enteredPIN):
                currentCustomer["attempts"] = 0
                while True:
                    print(f"Welcome {currentCustomer['name']}!")
                    optionSelected = displayMenu()
                    #Displaying the balance
                    if(optionSelected == 1):
                        print(f"Account balance is: ${'{:.2f}'.format(currentCustomer['balance'])}")
                    #Withdraw amount from account
                    if(optionSelected == 2):
                        currentCustomer['balance'] = withdrawal(currentCustomer['balance'])
                    #Depositing into the account balance
                    if(optionSelected == 3):
                        currentCustomer["balance"] = deposit(currentCustomer["balance"])
                    if(optionSelected == 4):
                        exitingProgram()
                    try:
                        anotherAction = input("Would you like to do another action? (y/n): ")
                        if(anotherAction.lower() == "n"):
                            exitingProgram()
                    except ValueError:
                        print("Invalid input. Please enter 'y' or 'n'.")
            else:
                print("Incorrect PIN. Please try again.")
                currentCustomer["attempts"] += 1

        else:
            #After 3 incorrect attempts together
            print("Too many incorrect attempts. Exiting. ")
            currentCustomer["status"] = "locked"
            exit()
except:
    if(enteredAccount not in [1,2,3]):
        print("Invalid account number")


        
    