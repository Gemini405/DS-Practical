class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # Point the new node to current head
            self.head.prev = new_node  # Link the current head's prev to the new node
            self.head = new_node       # Update head to the new node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Link current tail's next to new node
            new_node.prev = self.tail  # Link new node's prev to current tail
            self.tail = new_node       # Update tail to the new node

    # Function to delete the first node
    def delAtBegin(self):
        if self.head is None:  # If list is empty
            print("The list is empty, no element to delete.")
            return
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next  # Update head to the next node
            self.head.prev = None  # Remove reference to the old head

    # Function to delete the last node
    def delAtEnd(self):
        if self.tail is None:  # If list is empty
            print("The list is empty, no element to delete.")
            return
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev  # Update tail to the previous node
            self.tail.next = None  # Remove reference to the old tail

    # Function to delete a node with specific data (in the middle)
    def delInMid(self, data):
        if self.head is None:  # If list is empty
            print("The list is empty, no element to delete.")
            return
        temp = self.head
        while temp:  # Traverse to find the node
            if temp.data == data:
                # Node to be deleted is the only node
                if temp == self.head and temp == self.tail:
                    self.head = self.tail = None
                # Node to be deleted is the head
                elif temp == self.head:
                    self.delAtBegin()
                # Node to be deleted is the tail
                elif temp == self.tail:
                    self.delAtEnd()
                else:
                    temp.prev.next = temp.next  # Bypass the node
                    temp.next.prev = temp.prev  # Bypass the node
                return
            temp = temp.next
        print(f"Node with data {data} not found.")

# Testing the Doubly Linked List with delete functions
dll = DoublyLinkedList()
dll.insertAtBegin(10)
dll.insertAtEnd(20)
dll.insertAtBegin(5)
dll.insertAtEnd(30)
dll.insertAtEnd(40)
dll.printList()

print("\nAfter deleting at the beginning:")
dll.delAtBegin()
dll.printList()

print("\nAfter deleting at the end:")
dll.delAtEnd()
dll.printList()

print("\nAfter deleting a node in the middle (20):")
dll.delInMid(20)
dll.printList()

print("\nAfter trying to delete a node that doesn't exist (100):")
dll.delInMid(100)
