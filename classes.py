


class user:
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cash = 0
    
    def banking(self, account):
        self.cash += account
        return self
    
    def withdrawl(self, value):
        self.cash -= value
        return self
    
    def user_balance(self):
        print(self.first_name)
        print(self.cash)
        return self
   
    def transfer_money(self,amount,user):
        self.cash -= amount
        user.cash += amount
        self.user_balance()
        return self
        


user1 = user("Jared", "Peck", "jared.peck@uconnedu")
user2 = user("Chris", "Peck", "Chris.getwhatihave")
user3 = user("Evan", "Peck", "Evan.bear")



user1.banking(88).banking(77).banking(88).banking(88).withdrawl(99)
user2.banking(88).banking(88).banking(6543).banking(99876).withdrawl(543)
user2.banking(7765).banking(66).banking(543).banking(6546).withdrawl(98)
