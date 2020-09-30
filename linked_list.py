'''
class Node which creates New Nodes
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
'''
class Linked List
'''
class LinkedList:
    def __init__(self):
        self.head = None
    '''
    this function add the node at the begining of the Linked List
    '''
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    '''
    this function add the node at the end of the list
    '''
    def append(self,data):
        node = Node(data)
        #if list is empty
        if self.head is None:
            self.node = node
            return
        #iterate till head at last node
        last = self.head
        while last.next:
            last = last.next
        last.next = node
    def print(self):
        t = self.head
        while t:
            print(t.data,end=' ')
            t = t.next
'''
Main Function
'''
if __name__ == "__main__":
    l = LinkedList()
    n = int(input())
    m=n
    print("Push Operation")
    while n >0:
        l.push(int(input()))
        n -= 1
    print("Append Operation")
    while m>0:
        l.append(int(input()))
        m -=1
    print("Linked list:")
    l.print()
