"""
Open Closed Principle (OCP)
Software components should be closed for modification, but open for extension. (Plug and Play)
"""

# Dont do it
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
        
    def give_discount(self):
        if self.customer == "gold":
            return self.price * 0.7
        if self.customer == "silver":
            return self.price * 0.6
        return self.price * 0.2


""" 
Just think: in the future you have 20 different customer type, 
when add a new customer type you need add new condition for calculate discount, 
this situation totally violates OCP.
"""

# Do it
class NewDiscount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
        
    def get_discount(self):
        return self.price * 0.2

class GoldMemberDiscount(Discount):
    def get_discount(self):
        return self.price * 0.7
    
class SilverMemberDiscount(Discount):
    def get_discount(self):
        return self.price * 0.6

class PlatinumMemberDiscount(Discount):
    def get_discount(self):
        return self.price * 0.9
    
"""
Now if you want to add new customer type, you just need to add new class and get_discount method.
"""