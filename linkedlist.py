class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linked:
    def __init__(self):
        self.head = None
    def insert_b(self,data):
        node = Node(data, self.head)
        self.head = node
    def insert_e(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert(self,data):
        self.head = None
        for i in data:
            self.insert_e(i)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        s=''
        while itr:
            #s += str(itr.data)+'--->'
            print(itr.data,end=' ')
            print('--->',end=' ')
            itr = itr.next
        #print(s)
    def length(self):
        c=0
        i = self.head
        while i:
            c+=1
            i=i.next
        return c
    def remove(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Exception")
        if index == 0:
            self.head = self.head.next
            return
        count =0
        i = self.head
        while i:
            if count  == index -1:
                i.next = i.next.next
                break
            i = i.next
            count += 1
    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        i = self.head
        c =0
        while i:
            if c == index-1:
                node = Node(data,i.next)
                i.next = node
                break
            i = i.next
            c +=1


if __name__=="__main__":
    l =Linked()
    l.insert_b(132132)
    l.insert_e("end")
    l.print()
    print("\n length is ",l.length())
    l.insert_at(1,"Three")
    l.print()


