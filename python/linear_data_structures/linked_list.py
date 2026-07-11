class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.lengthOfList = 0

    def insert_at_beginning(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.lengthOfList += 1

    def insert_after_node(self, position, data):
        if not self.lengthOfList:
            print("Empty List")
            return
        if position >= self.lengthOfList:
            print("Invalid position")
            return
        
        currentPos = 1
        currentNode = self.head
        while True:
            if currentPos == position:
                node = Node(data)
                node.next = currentNode.next
                currentNode.next = node
                self.lengthOfList += 1
                break
            else:
                currentNode = currentNode.next
                currentPos += 1

    def insert_at_end(self, data):
        if self.lengthOfList == 0:
            print("No end for empty List")
            return
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        node = Node(data)
        currentNode.next = node
        self.lengthOfList += 1 

    def remove_by_position(self, position):
        if not self.head:
            print("Empty list")
            return
        if self.lengthOfList == 1 and position == 1:
            self.head = None
            self.lengthOfList -= 1
            return
        if self.lengthOfList == position:
            prevNode = None
            currentNode = self.head
            while currentNode.next != None:
                prevNode = currentNode
                currentNode = currentNode.next
            
            prevNode.next = None
            self.lengthOfList -= 1
            return
        if position > self.lengthOfList:
            print("Invalid position")
            return

        currentPos = 1
        prevNode = None
        currentNode = self.head

        while currentNode.next != None:
            if currentPos == position:
                prevNode.next = currentNode.next
                currentNode.next = None
                self.lengthOfList -= 1
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentPos += 1

    def printList(self):
        currentNode = self.head
        
        if self.head == None:
            print("Empty list")
            return
        if self.lengthOfList == 1:
            print(f"{self.head.data}")
            return

        while currentNode.next != None:
            print(currentNode.data, end = ' -> ')
            currentNode = currentNode.next
        print(currentNode.data)

class DoubleNode:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.lengthOfList = 0

    def insert_at_beginning(self, data):
        node = DoubleNode(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node 
            self.head = node
        self.lengthOfList += 1

    def insert_after_node(self, position, data):
        if not self.lengthOfList:
            print("Empty list")
            return
        if position >= self.lengthOfList:
            print("Invalid Position")

        currentPos = 1
        currentNode = self.head 

        while True:
            if currentPos == position:
                node = DoubleNode(data)
                nextNode = currentNode.next

                nextNode.prev = node
                node.next = nextNode
                currentNode.next = node
                self.lengthOfList += 1
                break
            else:
                currentNode = currentNode.next
                currentPos += 1

    def insert_at_end(self, data):
        if self.lengthOfList == 0:
            print("No end for empty list.")
            return
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        node = DoubleNode(data)
        node.prev = currentNode
        currentNode.next = node
        self.lengthOfList += 1

    def remove_by_position(self, position):
        if not self.head:
            print("Empty List")
            return
        if self.lengthOfList == 1 and position == 1:
            self.head = None
            self.lengthOfList -= 1
            return
        if self.lengthOfList == position:
            prevNode = None
            currentNode = self.head

            while currentNode.next != None:
                prevNode = currentNode
                currentNode = currentNode.next 

            prevNode.next = None
            self.lengthOfList -= 1
            return
        if position > self.lengthOfList:
            print("Invalid position")
            return

        currentPos = 1
        prevNode = None
        currentNode = self.head

        while currentNode.next != None:
            if currentPos == position:
                prevNode.next = currentNode.next
                currentNode.next.prev = prevNode
                self.lengthOfList -= 1
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentPos += 1

    def printList(self):
        if self.head == None:
            print("Empty list")
            return
        if self.lengthOfList == 1:
            print(f"{self.head.data}")
            return
       
        currentNode = self.head

        while currentNode.next != None:
            print(currentNode.data, end = ' <--> ')
            currentNode = currentNode.next
        print(currentNode.data)

if __name__ == "__main__":
    # Example of singleLinkedList, similar syntax follows for doubleLinkedList

    sll = SingleLinkedList()
    sll.insert_at_beginning("Head Node")
    sll.insert_at_end("End Node")
    sll.insert_after_node(1, "Node 2")
    sll.insert_after_node(2, "Node 3")
    sll.printList()

    sll.remove_by_position(4)
    sll.remove_by_position(2)
    sll.printList()
