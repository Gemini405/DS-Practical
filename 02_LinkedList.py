class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    def insertAtBegin(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            temp = self.head
            new_node = Node(item)
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def delAtBegin(self):
        if self.head is not None:
            self.head = self.head.next

    def delAtEnd(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delInMid(self, target):
        temp = self.head
        while temp.next.data is not target:
            temp = temp.next
        temp.next = temp.next.next

if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.insertAtBegin(10)
    llist.insertAtEnd(20)
    llist.insertAtEnd(30)
    llist.insertAtEnd(40)
    llist.insertAtEnd(50)
    llist.insertAtEnd(60)
    llist.traverse()

    llist.delAtBegin()
    llist.traverse()

    llist.delAtEnd()
    llist.traverse()

    llist.delInMid(30)
    llist.traverse()
