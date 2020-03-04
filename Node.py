class Node:
    def __init__(self, data, nextPointer=None):
        self.data = data
        self.nextPointer = nextPointer

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNextPointer(self, nextPointer):
        self.nextPointer = nextPointer

    def getNextPointer(self):
        return self.nextPointer
