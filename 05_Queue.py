class Queue:
    def __init__(self) -> None:
        self.queue = []

    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f'Item added to the queue: {item}')
    
    def dequeue(self):
        if self.size() < 1:
            return None
        
        return self.queue.pop()
    
    def display(self):
        print(self.queue)

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print('\nQueue:')
q.display()

q.dequeue()

print('\nAfter removal of an item:')
q.display()
