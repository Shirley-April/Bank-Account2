from datetime import datetime
class Account:
    def __init__(self, first_name, last_name, Phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.Phone_number = Phone_number
        self.withdrawals = []
        self.deposits =[]
        self.balance = 0
        self.loan = 0
        self.loan_repayments = []
        self.paybil_number4444 = []
        

    def account_name(self):
        name = "  account for {} {}".format(self.first_name, self.last_name)
        return name

    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
         
        else:
            self.balance += amount
            time = datetime.now()
            deposit = {
                "time": time,
                "amount": amount
            }
            self.deposits.append(deposit)
            formatted_time = time.strftime("%H:%M%p %d/%m/%Y")
            print("You have deposited {} to {} on {}".format(amount, self.account_name(), formatted_time))
            
    def withdraw(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")

        elif amount > self.balance:
            print("You have insufficient funds to withdraw this amount")
        
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))

    def get_balance(self):
     return "The balance for {} is {}".format(self.account_name(), self.balance)

    def get_formatted_time(self, time):
        return time.strftime("%H:%M%p %d/%m/%Y")

    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%H:%M%p %d/%m/%Y")
            print("{} deposited on {}".format(deposit, formated_time))
 
    def show_withdrawals_statement(self):
        for withdraw in  self.withdrawals:
            time = withdraw["time"]
            formated_time = self.get_formatted_time(time)
            amount = withdrawal["amount"]
            statement = "You withdrew {} on {}".format(amount, formated_time)
            print(withdraw)

    def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot request for an amount low than zero")
        else:
             self.loan = amount
             print("You have been given a loan of {}".format(amount))

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("Too low t repa your amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            time = datetime.now()
            repayment = {
                "time": time,
                "amount": amount
            }
            self.loan_repayments.append(repayment)
            print("You have repaid you loan with {} your balance is {}".format(amount, self.loan))
    
    def loan_repayment_statement(self):
        for repayment in self.loan_repayments:
            time = repayment["time"]
            amount = repayment["amount"]
            formatted_time = self.get_formatted_time(time)
            statement = "You repaid {} on {} ".format(amount, formatted_time)
            print(statement)

class BankAccount(Account):
    def __init__(self, first_name, last_name,Phone_no, bank):
        self.bank = bank
        super().__init__(first_name, last_name, Phone_no)

class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, Phone_no, service_provider):
        self.airtime = []
        super().__init__(first_name, last_name, Phone_no)

    def buy_airtime(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You dont have enough balance. Your balnce is {}".format(self.balance))
        else:
            self.balance -= amount 
            time =datetime.now()
            airtime = {
                "time": time,
                "airtime": amount
            }
            self.airtime.append(airtime)
            print("You have bought airtime worth of {} on {} ".format(amount, self.get_formatted_time(time)))
    
    def paybill(self, amount):
        paybill_number = "4444"
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount inn figures")
            return

        if amount <= 0:
            print("You cannot pay with a zero!")
        elif amount > self.balance:
            print("Insufficient fund to pay this bill ")
        else:
            self.balance -= amount
            self.paybil_number4444.append(amount)
            print(" {} sent!  to pabill number {} from {} ".format(amount, paybill_number, self.account_name()))


    def send_money(account1, account2, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return
        account1.withdraw(amount)
        account2.deposit(amount)
        print("You have transfered {} ".format(amount))

    def recieve_money(account1, account2, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return
        var1 = account2.withdraw(amount)
        var2 = account1.deposit(amount)
        print("You have recieved {} ".format(amount, ))
        
