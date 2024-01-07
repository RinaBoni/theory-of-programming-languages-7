
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insert_at_begin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of LL

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
        # at given position
    def update_node(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def size_of_LL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def print_LL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
    # Метод для получения следующего узла
    def get_next_node(self, node):
        if node is not None and node.next is not None:
            return node.next
        else:
            return None
        
    # Метод для передвижения указателя на следующий узел
    def move_to_next_node(self, current_node):
        if current_node is not None and current_node.next is not None:
            return current_node.next
        else:
            return None

    def add_elements_from_list(self, elements_list):
        for element in elements_list:
            self.insert_at_end(element)
    
    def get_token_names(self):
        token_names = []
        current_node = self.head

        while current_node:
            # Получение значения token_name из текущего элемента
            token_name = current_node.data.get('token_name')
            
            # Добавление значения token_name в список
            token_names.append(token_name)

            # Переход к следующему элементу
            current_node = current_node.next

        return token_names
    
    def get_head(self):
        current_node = self.head
        return current_node
    
    
# Создание связанного списка
linked_list = LinkedList()

# Добавление элементов в связанный список (пример)
linked_list.insert_at_end({'token_name': 'IDENT', 'token_value': 'i', 'index': 5})
linked_list.insert_at_end({'token_name': 'NUMBER', 'token_value': '42', 'index': 6})
linked_list.insert_at_end({'token_name': 'KEYWORD', 'token_value': 'for', 'index': 7})

# Получение значений token_name из связанного списка
token_names = linked_list.get_token_names()

