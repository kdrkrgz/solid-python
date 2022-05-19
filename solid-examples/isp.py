"""
Interface Segregation Principle (ISP)
No clients should be forced to depend on methods it does not use
*** All Methods must make sense for all classes

How to recognize violations:
1- Fat Interfaces (PhoneFunctions class is fat)
2- Interfaces with low cohesion and violates SRP (PhoneFunctions class have different features)
3- Empty Method Implementations
"""

# Dont do it


class PhoneFunctions:
    def call(self):
        raise NotImplementedError()

    def text(self):
        raise NotImplementedError()

    def browse(self):
        raise NotImplementedError()


class MobilePhone(PhoneFunctions):
    def call(self):
        print("Calling")

    def text(self):
        print("Texting")

    def browse(self):
        print("Browsing")


class DeskPhone(PhoneFunctions):
    def call(self):
        print("Calling")

    def text(self):
        pass

    def browse(self):
        pass


mobile_phone = MobilePhone()
mobile_phone.text()

desk_phone = DeskPhone()
desk_phone.text()


"""
Deskphone doesnt have texting and browsing features, but it was inherited from PhoneFunctions class.
So it has all the features of PhoneFunctions class but it cant all
"""
# Do it


class Call:
    def call(self):
        raise NotImplementedError()


class Text:
    def text(self):
        raise NotImplementedError()


class Browse:
    def browse(self):
        raise NotImplementedError()


class MobilePhone(Call, Text, Browse):
    def call(self):
        print("Calling")

    def text(self):
        print("Texting")

    def browse(self):
        print("Browsing")


class DeskPhone(Call):
    def call(self):
        print("Calling")


mobile_phone = MobilePhone()
mobile_phone.browse()

desk_phone = DeskPhone()
desk_phone.call()
