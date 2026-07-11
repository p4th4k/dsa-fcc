from linked_list import SingleLinkedList

''' 
Stack | Queue 
- Access by index : O(n) | O(n)
- Search          : O(n) | O(n)
- Push/Pop        : O(1) | O(1)
- Enqueue/Dequeue : O(1) | O(1)
'''

class Stack:
    ''' LIFO '''
    def __init__(self):
        self.stack = SingleLinkedList()

    def push(self, data):
        if self.stack.lengthOfList == 0:
            self.stack.insert_at_beginning(data)
            return
        self.stack.insert_at_end(data)

    def pop(self):
        self.stack.remove_by_position(self.stack.lengthOfList)

    def printStack(self):
        self.stack.printList()

class Queue:
    ''' FIFO '''
    def __init__(self):
        self.queue = SingleLinkedList()

    def enqueue(self, data):
        self.queue.insert_at_beginning(data)

    def dequeue(self):
        self.queue.remove_by_position(self.queue.lengthOfList)

    def printQueue(self):
        self.queue.printList()
