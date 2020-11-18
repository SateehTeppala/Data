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

    def insert(self,newnode):
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
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next


if __name__ == '__main__':
    n = int(input("How many Nodes U want to insert..?:>"))
    ll = LinkedList()
    for i in range(n):
        d = input()
        data = Node(d)
        ll.insert(data)
    print("LinkedList is:")
    ll.print()
