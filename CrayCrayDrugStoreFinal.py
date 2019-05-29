from CustomerClass import Customer
import numpy as np
import NodeQueue
import PriorityQueue


class CrayCrayDrugStore():

    rotated = False
    counter = 0

    def __init__(self):
        self.CustomerQueue = NodeQueue.NodeQueue()
        self.SeniorQueue = PriorityQueue.PriorityQueue()
        self.CustomerList = []

    def FindCustomer(self, name):
        for cust in self.CustomerList:
            if(str(cust) == name):
                return f'Customer: {name}\nAge: {cust.age}'
        return name + ' is not in the Customer List.'

    def addToCusList(self, node):
        if node not in self.CustomerList:
            self.CustomerList.append(node)

    def stringFixer(self, stringz):
        temp = list(stringz.split(' '))
        newstring = ''
        counter = 0
        for item in temp:
            new = item[0].capitalize() + item[1:].lower()
            if counter != 0:
                newstring += '-'
            newstring += new
            counter += 1
        return newstring

    def Lineup(self, name, age):
        global rotated
        if any(x.name == name for x in self.CustomerQueue.queue) or any(x.name == name for x in self.SeniorQueue.queue):
            print('Unable to line up: Name Duplicate Error')
        else:
            newname = self.stringFixer(name)
            newcus = Customer(newname, age)
            self.addToCusList(newcus)
            if newcus.age < 65:
                self.CustomerQueue.queue.append(newcus)
            else:
                if self.rotated is True:
                    if len(self.SeniorQueue.queue) > 0:
                        index = 0
                        for indx, senior in enumerate(self.SeniorQueue.queue):
                            if newcus.age == senior.age:
                                index = indx
                            elif (newcus.age < senior.age):
                                index -= 1
                        b = self.SeniorQueue.queue[:index] + [newcus] + self.SeniorQueue.queue[index:]
                        self.SeniorQueue.queue = b
                else:
                    if len(self.SeniorQueue.queue) > 0:
                        index = 0
                        for indx, senior in enumerate(self.SeniorQueue.queue):
                            if newcus.age == senior.age:
                                index = indx
                            elif (newcus.age < senior.age):
                                index = indx + 1
                        b = self.SeniorQueue.queue[:index] + [newcus] + self.SeniorQueue.queue[index:]
                        self.SeniorQueue.queue = b
                    else:
                        self.SeniorQueue.queue.append(newcus)
            print(newname + ' has lined up.')

    def Serve(self):
        toServe = None
        if len(self.SeniorQueue.queue) != 0:
            seniorQages = (senior.age for senior in self.SeniorQueue.queue)
            toServe = np.argmin(seniorQages)
            print(str(self.SeniorQueue.queue[toServe]) + ' has been served.')

            del self.SeniorQueue.queue[toServe]
        else:
            if len(self.CustomerQueue.queue) != 0:
                print(str(self.CustomerQueue.queue[0]) + ' has been served.')
                del self.CustomerQueue.queue[0]

            else:
                print('There are no customers to serve!')

    def Rotate(self):
        global rotated
        global counter
        self.SeniorQueue.queue = self.SeniorQueue.queue[::-1]
        self.CustomerQueue.queue = self.CustomerQueue.queue[::-1]
        self.counter += 1

        if self.counter % 2 != 0:
            self.rotated = True
        else:
            self.rotated = False

        print('Cray Cray DrugStore has been rotated!')

    def Display(self):
        custlist = 'Current Customer List: | '
        for cust in self.CustomerList:
            custlist += str(cust) + ' | '
        print('Current Customer List: ' + custlist)
        if len(self.CustomerQueue.queue) != 0:
            custQlist = 'Current Customer Queue: | '
            for cust in self.CustomerQueue.queue:
                    custQlist += str(cust) + ' | '
            print(custQlist)
        else:
            print('Customer Queue empty.')

        if len(self.SeniorQueue.queue) != 0:
            senQlist = 'Current Senior Queue: | '
            for cust in self.SeniorQueue.queue:
                    senQlist += str(cust) + ' | '
            print(senQlist)
        else:
            print('Senior Queue empty.')

    def printCustomerQueue(self):
        print('current Customer Queue: ' + str(self.CustomerQueue))

    def printSeniorQueue(self):
        print('current senior queue: ' + str(self.SeniorQueue))

    def printCustList(self):
        print('current Customer List: ' + str(self.CustomerList))

    def Exit(self):
        print('Goodbye!')
