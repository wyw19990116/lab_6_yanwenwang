from Node import Node


class LinkedList:
    def __init__(self, head=None, size=1, tail=None):
        self.head = head
        self.size = size
        self.tail = tail

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def setTail(self, tail):
        self.tail = tail

    def getTail(self) :
        if self.tail is None:
            return self.head
        return self.tail

    def isEmpty(self):
        return self.getSize() > 0

    def addNode(self, data):
        node = Node(data)
        if self.isEmpty():
            self.setHead(node)
        else:
            self.getTail().setNextPointer(node)
        self.setTail(node)
        self.setSize(self.size + 1)


if __name__ == '__main__':
    list = LinkedList()
    list.addNode(1000)
    print("head", list.getHead().getData())
    print("tail", list.getTail().getData())
    list.addNode(2000)
    print("head", list.getHead().getData())
    print("tail", list.getTail().getData())
