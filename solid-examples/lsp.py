"""
Liskov Substitution Principle (LSP)
Objects should be replaceable with their subtypes without altering the correctness of the program.

*** Ostrich is a bird, BUT ostrich cannot fly

****** If it looks like a duck and quacks like a duck but it need batteries, you probably have the wrong abstraction

How to make:

If the super-class (Bird) has a method that accepts a super-class type (Bird) parameter. 
Its sub-class(Ostrich) should accept as argument a super-class type (Bird type) or sub-class type(Ostrich type).
If the super-class returns a super-class type (Bird). 
Its sub-class should return a super-class type (Bird type) or sub-class type(Ostrich).

"""

### Break the Hiearchy
# Dont do it
class Bird:
    def fly(self):
        pass
    
    
class Ostrich(Bird):
    def fly(self):
        raise RuntimeError("Ostrich cannot fly")
    
class Duck(Bird):
    def fly(self):
        print("I'm flying")
    
birds = [Duck(), Ostrich()]

def fly_birds(birds:list):
    for bird in birds:
        bird.fly()
        
fly_birds(birds)
        
"""
If u want to change the Ostrich class to a bird class, that will fail when try to fly method
**** Break the hierarchy if it fails the substitution test
"""
#! Eğer elimde bir kuş varsa kuşa ait tüm özelliklerini kullanabilmeliyim hangi kuşun hangi özelliği olduğunu/olmadığını bilmek zorunda değilim.
# Do it
class Bird:
    def eat(self):
        raise NotImplementedError()

        
class Ostrich(Bird):
    def _eat_grass(self):
        print("I'm eating grass")
        
    def eat(self):
        self._eat_grass()


class Duck(Bird):        
    def _eat_fish(self):
        print("I'm eating fish")

    def eat(self):
        self._eat_fish()
        
        
def feed_birds(birds:list):
    for bird in birds:
        bird.eat()
        
birds = [Duck(), Ostrich(), Duck(), Duck()]

feed_birds(birds)



### Tell Don't Ask
# Don't do it
class Product:
    def __init__(self, discount):
        self.discount = discount 
    
    def get_discount(self):
        print(self.discount)


class InHouseProduct(Product):
    def apply_extra_discount(self):
        print(self.discount * 1.5)


def get_discounts(products:list):
    for product in products:
        if isinstance(product, InHouseProduct):
            product.apply_extra_discount()
            continue
        product.get_discount()
        
products = [InHouseProduct(0.2), Product(0.3), Product(0.4)]
get_discounts(products)


# Do it
"""
if override the get_discount method, you can use for all product, 
dont know product type, and without checking the type
"""
class Product:
    def __init__(self, discount):
        self.discount = discount 
    
    def get_discount(self):
        print(self.discount)


class InHouseProduct(Product):
    @staticmethod    
    def _apply_extra_discount(discount):
        print(discount * 1.5)

    def get_discount(self):
        return self._apply_extra_discount(self.discount)

def get_discounts(products:list):
    for product in products:
        product.get_discount()
        
products = [InHouseProduct(0.2), Product(0.3), Product(0.4)]
get_discounts(products)

# İndirimi uygulasını söyle, indirimi nasıl uyguladığını sorma!