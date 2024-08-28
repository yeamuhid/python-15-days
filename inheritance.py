class   Vehicle:
    def general_use(self):
        print("General use: transporation")
class Car(Vehicle):

    def __int__(self):
        print("I am car")
        self   .wheels =4
        self . has_roof= True

    def specific_usage(self):
        print("Specific usage: famaily use")




class Motorcycle(Vehicle):
    def __int__(self):
        print("I am motorcycle")
        self .wheels =2
        self . has_roof= False

    def specific_usage(self):
        print("Specific usage: personal use or sports")

c= Car ()
c.specific_usage()
c.general_use()

m= Motorcycle()
m.specific_usage()
m.general_use()

