from NodeQueue import NodeQueue


class PriorityQueue(NodeQueue):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def show(self):
        print('Current Customer Queue: ' + ''.join(str(cust) for cust in self.CustomerQueue))
        pass
