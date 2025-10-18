class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Print linked list
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Add new node at end of linked list
        """
        new_node = Node(value)
        if self.length == 0: # self.head is None
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Remove node from end of linked list
        """
        if self.head is None: # empty linked list
            return None
        temp = self.head
        if self.head.next is None: # Only one item in linked list
            self.head = self.tail = None
            self.length -= 1
            return temp
        # more than one item in linked list
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length -= 1
        return temp
    
    def prePend(self, value):
        """
        Insert item at start of linkedlist
        """
        new_node = Node(value)
        if self.head is None: # empty linked list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        """
        Remove node from end of linked list
        """
        if self.head is None: # empty linked list
            return None
        temp = self.head
        if self.head.next is None: # Only one item in linked list
            self.head = self.tail = None
            self.length -= 1
            return temp
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp
    
    def get_node(self, index):
        """
        Get node based on index
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        """
        Set value based on index
        """
        temp = self.get_node(index=index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prePend(value=value)
        if index == self.length:
            return self.append(value=value)
        new_node = Node(value)
        prev_node = self.get_node(index-1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Remove item from specific index
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get_node(index - 1)
        current_node = prev_node.next
        prev_node.next = current_node.next
        current_node.next = None
        self.length -= 1
        return current_node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(100)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

print("\nAppend new node with value 200")

my_linked_list.append(200)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nAfter pop operation ")

print("Item removed :")
node = my_linked_list.pop()
if node:
    print(node.value)
else:
    print(None)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nPop if only 1 item left in linked list")

print(my_linked_list.pop())

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nPop if nothing left in linked list")

print(my_linked_list.pop())

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nInserting 100 at start :")

my_linked_list.prePend(100)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nInserting 200 at start :")

my_linked_list.prePend(200)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nInserting 300 at start :")

my_linked_list.prePend(300)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nGet item at index 2 :")
node = my_linked_list.get_node(2)
if node:
    print(node.value)
else:
    print(node)

print("\nSet 500 at index 1 :")
my_linked_list.set_value(index=1, value=500)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nInsert 900 at index 2 :")
my_linked_list.insert(index=2, value=900)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nReversing linked list : ")
my_linked_list.reverse()

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nRemoving index 2 from linked list :")
node = my_linked_list.remove(index=2)
if node:
    print(node.value)
else:
    print(None)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nRemoving index 1 from linked list :")
node = my_linked_list.remove(index=1)
if node:
    print(node.value)
else:
    print(None)

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nRemoving 1st item from linked list with 2 nodes")
my_linked_list.popFirst()

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nRemoving 1st item from linked list with 1 node")

my_linked_list.popFirst()

print("Linked list is :", sep=" ")
my_linked_list.print_list()

print("\nRemoving 1st item from empty linked list")

my_linked_list.popFirst()

print("Linked list is :", sep=" ")
my_linked_list.print_list()
