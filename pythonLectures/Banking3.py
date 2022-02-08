
class Banking:
    
    def __init__(self,int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return self 
    
    def Withdrwal(self,amount):
        if amount >= self.balance:
            return "insufficient funds"
        else:
            self.balance -= amount
            return self 
    
    def yeild(self):
        x = 0 
        if self.balance > 0:
            x = self.balance * self.int_rate
            self.balance += x
            print(str(self.balance) + " rate with interest added")
        return self
    
    def __str__(self):
        return "balance " + str(self.balance)  




class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = Banking(.005,888)  
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdrawl(self,amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        




Jared = User("Jared")
Chris = User("Chris")
bob = User("Bob")

