class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self) -> None:
        print("---")
        print("Length: ", self.length)
        if self.head:
            print("Head node - ", self.head.__dict__)
        if self.tail:
            print("Tail node - ", self.tail.__dict__)
        temp = self.head
        while temp is not None:
            print(temp.__dict__)
            temp = temp.next
        print("---")

    def append(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # It's a previous node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        node = self.head
        pre = self.head
        while node.next is not None:
            pre = node
            node = node.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return True

    def get_node_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node
        # element = self.head
        # if index < 0:
        #     print("Can't get element by Negative indexing.")
        #     return
        # print(f"Element at index {index}: ")
        # while element is not None and index >= 0:
        #     if index == 0:
        #         print(element.value)
        #         return element.value
        #     element = element.next
        #     index -= 1
        # raise(IndexError('Linked list index out of range.'))

    def change_node_by_index(self, index, value):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        node.value = value
        return node
        
    def insert_node_by_index(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        pre_node = self.get_node_by_index(index - 1)
        new_node.next = pre_node.next
        pre_node.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 and index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        pre_node = self.get_node_by_index(index - 1)
        next_node = pre_node.next
        pre_node.next = next_node.next
        self.length -= 1
        
        # Just to return the removed object
        next_node.next = None
        return next_node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after





my_linked_list = MyLinkedList(11)
my_linked_list.append(3)
my_linked_list.append(82)
my_linked_list.append(24)
my_linked_list.append(99)
my_linked_list.append(6)

my_linked_list.print()

my_linked_list.pop()
my_linked_list.pop()

print('After 2 pop operation')
my_linked_list.print()

my_linked_list.prepend(65)

print('After prepend operation')
my_linked_list.print()

my_linked_list.pop_first()

print("After pop first element")
my_linked_list.print()

print('Get item by index:', my_linked_list.get_node_by_index(2))
print('Change item by index:', my_linked_list.change_node_by_index(index = 2, value = 88))

print("\nAfter get and change value operations")
my_linked_list.print()

my_linked_list.insert_node_by_index(2, 15)
print('\nAfter inserting a node with value 15 at index 2')
my_linked_list.print()

my_linked_list.remove(index = 3)
print('\nAfter removing a node at index 1')
my_linked_list.print()

my_linked_list.reverse()
print('\nAfter revering the linked list:')
my_linked_list.print()