


class user:
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cash = 0
    
    def banking(self, account):
        self.cash += account
    
    def withrawl(self, value):
        self.cash -= value
    
    def user_balance(self):
        print(self.first_name)
        print(self.cash)
   
    def transfer_money(self,amount,user):
        self.cash -= amount
        user.cash += amount
        self.user_balance()
        


user1 = user("Jared", "Peck", "jared.peck@uconnedu")
user2 = user("Chris", "Peck", "Chris.getwhatihave")
user3 = user("Evan", "Peck", "Evan.bear")



 

user1.banking(77)




user2.banking(77)
user2.banking(99)
user2.withrawl(55)


user3.banking(1000)




user3.transfer_money(100,user1)

user1.user_balance()



