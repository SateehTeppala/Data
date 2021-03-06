'''
@author:Teppala Sa7eesh
name:Single LinkedList with all functions
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

    def delEnd(self):
        lastnode = self.head
        while lastnode.next is not None:
            previousnode = lastnode
            lastnode = lastnode.next
        previousnode.next = None

    def delHead(self):
        previousnode = self.head
        self.head = self.head.next
        previousnode.next = None

    def delAt(self,position):
        if position < 0 or position > self.getLength():
            print("Invalid position")
            return
        if self.head is not None:
            if position == 0:
                self.delHead()
                return
            currentnode = self.head
            currentpostion = 0
            while True:
                if currentpostion == position:
                    previousnode.next = currentnode.next
                    currentnode.next = None
                    break
                previousnode = currentnode
                currentnode = currentnode.next
                currentpostion +=1

    def reverseList(self):
        previousnode = None
        currentnode = self.head
        following = currentnode.next
        while currentnode:
            currentnode.next = previousnode
            previousnode = currentnode
            currentnode = following
            if following:
                following = following.next
        self.head = previousnode


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
    new = Node("one plus")
    ll.insertBegin(new)
    at = Node(1)
    ll.insertAt(at,3)
    ll.print()
    #ll.delAt(2)
    print('-------------------')
    ll.reverseList()
    ll.print()
    #ll.delEnd()
    #ll.print()




    '''
    n = int(input("How many Nodes U want to insert..?:>"))
    ll = LinkedList()
    for i in range(n):
        d = input()
        data = Node(d)
        ll.insertBegin(data)
    print("LinkedList is:")
    ll.print()

      '''
