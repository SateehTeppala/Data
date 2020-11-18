'''
@author:Teppala Sa7eesh
name:Single LinkedList
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    """docstring for LinkedList."""
    def __init__(self):
        self.head = None
    def getLength(self):
        currentnode = self.head
        len = 0
        while currentnode is not None:
            currentnode = currentnode.next
            len +=1
        return len
    def insertBegin(self,newnode):
        temp = self.head
        self.head = newnode
        self.head.next = temp
        del temp
    def insertAt(self,newnode,position):
        currentnode = self.head
        currentpostion = 0
        if position == 0:
            self.insertBegin(newnode)
            return
        if position < 0 or position > self.getLength():
            print("Invalid position")
            return
        while  True:
            if currentpostion == position:
                previousnode.next = newnode
                newnode.next = currentnode
                break
            previousnode = currentnode
            currentnode = currentnode.next
            currentpostion +=1

    def insertEnd(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode

    def print(self):
        if self.head is None:
            print("List is empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next


if __name__ == '__main__':
    one = Node("One")
    ll = LinkedList()
    ll.insertEnd(one)
    two = Node("Two")
    ll.insertEnd(two)
    three = Node("Three")
    ll.insertEnd(three)
    new = Node("New Head")
    ll.insertBegin(new)
    at = Node(1)
    ll.insertAt(at,3)
    ll.print()
    '''n = int(input("How many Nodes U want to insert..?:>"))
    ll = LinkedList()
    for i in range(n):
        d = input()
        data = Node(d)
        ll.insertBegin(data)
    print("LinkedList is:")
    ll.print()'''
