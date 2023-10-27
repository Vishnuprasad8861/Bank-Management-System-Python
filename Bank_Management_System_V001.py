##______________ Bank_Management_System______________________

print('''
  Welcome To YoYo Bank!!!!''')

print('''
    ______LOGIN_PAGE______''')
print("Welcome To Login Page")

def login(users):
    while True:
        User_Name=input("Please Enter Your UserName:")
        Password=input("Please Enter Your Password:")

        for x in users:
            if User_Name== x[0] and Password == x[1]:
                print(User_Name, " has Succesfully Loged In ")
                return User_Name
        else:

            print("Incorrect Password or Username Login Failed!! Try again Later" )

users= [['abhi_001','123@ab'],['shrey_456','546@we'],['donald123','808636']]
User_Name=login(users)


def Deposit(currentbalance_amount):
    deposit = int(input("Enter the amount to Deposit:"))
    currentbalance_amount += deposit

    print("Amount Deposit Successfully,\n"
          "Your Current Balance is:",currentbalance_amount)
    return currentbalance_amount

def Withdraw(currentbalance_amount):
    withdraw = int(input("Enter the amount to Withdraw:"))
    if withdraw <= currentbalance_amount:
        currentbalance_amount -= withdraw
        print("Amount Withdraw Successfully:",currentbalance_amount)
    else:
        print("Insufficient Amount,Failed to withdraw amount")
    return currentbalance_amount


def balance_enquiry(currentbalance_amount):
    print("Your Account Balance is:",currentbalance_amount)

currentbalance_amount=1000

while True:
    print('''
        -------Choose an Option-------''')

    print('..1.Deposit_Amount:\n'
          '..2.WithDraw_Amount:\n'
          '..3.Balance_Enquiry:\n'
          '..4.Exit ')


    choice=int(input("Enter The Option:"))

    if choice==1:
        currentbalance_amount=Deposit(currentbalance_amount)

    elif choice==2:
        currentbalance_amount=Withdraw(currentbalance_amount)

    elif choice==3:
        balance_enquiry(currentbalance_amount)

    elif choice==4:
        print(("Thank You For Using Bank System"))
        break
    else:
        print("You Entered a Invalid Choice")














