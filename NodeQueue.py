class NodeQueue():

    top = None
    last = None

    def __init__(self):
        self.queue = []
        self.root = None
        self.last = None

    def __repr__(self):
        return str(self.queue)

    def Enqueue(self, node):
        self.queue.append(node)

    def Dequeue(self, node):
        del self.queue[0]

    def Peek(self, node):
        return self.queue[len(self.queue) - 1]

    def show(self):
        print('Current Customer Queue: ' + ''.join(str(cust) for cust in self.queue))

    def clear(self):
        for item in self.queue:
            del item

    def findNode(self):
        pass
