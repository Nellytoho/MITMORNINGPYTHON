class people:
    def __init__(self, name, age, gender):
        self.personname = name
        self.personage = age
        self.persongender = gender

    def display(self):
        print(self.personname, self.personage, self.persongender)


myobj = people("Nelly", 18, "female")
myobj.display()
myobj = people("Harrison", 20, "Male")
myobj.display()
myobj = people("Joan", 11, "Female")
myobj.display()
