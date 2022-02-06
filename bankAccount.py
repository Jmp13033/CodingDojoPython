


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
            print(str(x) + " rate with interest added")
        return self

       
    def display(self):
        print(self.balance)
        return self
    


Jared = Banking(1.4,1000)
print(Jared.deposit(99).deposit(1000).deposit(77).Withdrwal(96).display().yeild())
John = Banking(1.3, 7000)
print(John.deposit(9000).deposit(1000).deposit(700).deposit(875).Withdrwal(1000).Withdrwal(1000).display().yeild())


















