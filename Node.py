from CustomerClass import Customer


class Node(Customer):

    next = None

    def __init__(self, name, age):
        Customer.__init__(self, name, age)
        self.name = name
        self.age = age

    def __repr__(self):
        return str(self.name)

    def GetElement(self):
        return self.name

    def GetNext(self):
        return self.next

    def SetElement(self, newvalue):
        self.name = newvalue

    def SetNext(self, newNext):
        self.next = newNext
