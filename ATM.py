#Veronica Stureborg
#Project 12
#ATM 
class BankAccount:
    def __init__(self, user, pin, checking, savings):
        self.user = user
        self.pin = pin
        self.checking = checking
        self.savings = savings

    def getUser(self):
        return self.user

    def getPin (self):
        return self.pin

    def getSavings(self):
        return self.savings

    def withdraw(self, amount):
        if(self.savings<amount):
            return False
        else:
            self.savings -=amount
        return True

    def deposit(self, amount):
        self.savings +=amount

def main():
    account= []
    n=0

    with open ('userfile.txt', 'r') as rf:
        for line in rf:
            li = line.split(' ')
            account.append(BankAccount(li[0], li[1], float(li[2]), float(li[3].replace('\n',''))))
            n+= 1
    username = input("Enter Username: ")
    password = input("Enter pin: ")
    i=0

    while i<n:
        if (account[i].getPin()==password):
            option = int(input("Enter 1 for withdraw, 2 for deposit, or 3 for balance: "))
            if (option==1):
                amount = float(input("Enter amount to withdraw: "))
                if (account[i].withdraw(amount)):
                    print ("$", amount, "withdrawn. New balance is: $", account[i].getSavings())
                else:
                    print("Cannot withdraw the amount requested. Enter a lower amount.")
            elif (option==2):
                amount = float(input("Enter amount: "))
                account[i].deposit(amount)
                print("The new balance after deposit is: $", account[i].getSavings())
            else:
                print("Your Savings balance is: $", account[i].getSavings())
            print("Thank You.")
            break
        i += 1
    if (i==n):
        print("Invalid Login")
    
main()
