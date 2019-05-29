class Customer():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age
