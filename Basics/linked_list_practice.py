# Node class for node definitions
class Node:
    # Node define
    def __init__(self, value):
        self.value = value
        self.next = None


# LinkedList class for methods definition
class LinkedList:
    # Linkedlist define
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print lineked list method
    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.value)
            temp = temp.next

    # Add new node at end of linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None: # empty linked list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # Remove a not from end of lined list
    def pop(self):
        if self.head is None: # empty linked list
            return None
        if self.head.next is None: # only node
            self.head = self.tail = temp = None
        else:
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            pre.next = None
            self.tail = pre
        self.length -= 1
        return temp
    
    # Add not at start of linked list
    def prePend(self, value):
        new_node = Node(value)
        if self.head is None: # empty linked list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # Remove 1st node of linked list
    def popFirst(self):
        if self.head is None: # empty linked list
            return None
        if self.head.next is None: # only node
            self.head = self.tail = temp = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
    
    # Get node based on index
    def get_node(self, index):
        if index < 0 or index > self.length - 1: # Index out of bound
            return None
        temp = self.head
        for _ in range(self.length):
            temp = temp.next
        return temp
    
    # Set a value to node of specific index
    def set_node(self, index, value):
        temp = self.get_node(index)
        if temp:
            temp.value = value
            return True
        return False

    # Add node at specific index
    def insert_node(self, index, value):
        if index < 0 or index > self.length: # Index out of bound
            return False
        if index == 0:
            return self.prePend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre_node = self.get_node(index - 1)
        new_node.next = pre_node.next
        pre_node.next = new_node
        self.length += 1
        return True
    
    # Remove node from specific index
    def remove_node(self, index):
        if index < 0 or index > self.length - 1:
            return False
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        pre_node = self.get_node(index - 1)
        current_node = pre_node.next
        pre_node.next = current_node.next
        current_node.next = None
        self.length -= 1
        return current_node

    # Reversing linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
        
