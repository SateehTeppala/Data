class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def print(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next


if __name__ == "__main__":
    l = LinkedList()
    n = int(input())
    while n >0:
        l.push(int(input()))
        n -= 1
    l.print()
