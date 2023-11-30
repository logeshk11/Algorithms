class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkLinst():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if  self.head is None:
            self.head = Node(data, None)

        else:
            itr = self.head
            while itr.next:
                itr=itr.next
            itr.next = Node(data, None)

    def insert_new_list(self, data_list):
        self.head=None
        for i in data_list:
            self.insert_at_end(i)

    def print(self):
        itr = self.head
        while itr:
            print(itr.data,end=" ")
            itr = itr.next



    def remove_index(self, i):
        if i == 0:
            self.head=self.head.next
            return

        itr = self.head
        count =0
        while itr:
            if count == i-1:
                itr.next=itr.next.next
            itr=itr.next
            count +=1

    def reverse_list(self):
        cur = self.head
        next = None
        pre = None
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        self.head=pre



li= LinkLinst()
li.insert_new_list([54,56,58,21,7,45,3,25])
li.print()
print()
li.reverse_list()
li.print()