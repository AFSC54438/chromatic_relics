from random import randint
from cs50 import get_int


# -----------------------------------------------------------------------------------------
# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linked List class
class Linked_List:
    def __init__(self):
        self.head = None

    # Insert Node method
    def insert(self, new_node):
        if not isinstance(new_node, Node):
            raise ValueError("Not a node")

        if self.head is None or new_node.value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    # Remove Node method
    def remove(self, value_to_remove):
        if self.head is None:
            raise ValueError("Node is empty")

        if self.head.value == value_to_remove:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value_to_remove:
                current.next = current.next.next
                return
            current = current.next

    # Print Linked List method
    def display(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))


# -----------------------------------------------------------------------------------------
# Testing

# Get numbers to be inserted to linked list
my_nums = []

while len(my_nums) < 10:
    num = randint(-50, 50)
    if num not in my_nums:
        my_nums.append(num)

print(f"Numbers: {sorted(my_nums)}")

# Declare linked list
my_link_list = Linked_List()

# Converting numbers to nodes & inserting to linked list
for n in my_nums:
    my_link_list.insert(Node(n))

# Printing linked list
print()
print("Linked List: ")
my_link_list.display()

# Inserting & removing a new value
new_val = get_int("Insert a number to linked list: ")
my_link_list.insert(Node(new_val))
my_link_list.display()

# Inserting & removing a new value
remove_val = get_int("Remove a value from linked list: ")
my_link_list.remove(remove_val)
my_link_list.display()
