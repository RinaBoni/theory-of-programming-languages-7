class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def tree_size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.tree_size(node.left) + self.tree_size(node.right)
        
    def hash_function(self, key):
        hash_value = 0
        for charq in key:
            hash_value += ord(charq)
        return hash_value

    def search(self, root, key):
        # Если корень пуст или ключ находится в корне
        if root is None or root.key == key:
            return root

        # Если ключ меньше значения корня, идем налево
        if key < root.key:
            return self.search(root.left, key)

        # Иначе идем направо
        return self.search(root.right, key)
    
    
    # def save_list_to_file(file_path, data):
   
    #     with open(file_path, 'w') as file:
    #         for item in data:
    #             file.write(str(item) + '\n')
                
    def read_list_from_file(file_path):
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file.readlines()]
        return data

    def save_list_to_file(self, file_path, data):
        with open(file_path, 'w') as file:
            file.truncate(0)
            for item in data:
                file.write(str(item) + '\n')
    
import random


b = BstNode(50)

file_path = 'identifiers.txt'

with open(file_path, 'r') as file:
        identifier_data = [line.split() for line in file.read().splitlines()]

for index, (identifier) in enumerate(identifier_data, start=1):
    identifier_hash = b.hash_function(identifier)
    b.insert(identifier_hash)
    print(f"Идентификатор {identifier} добавлен в таблицу. Индекс: {index}")
    # print(f"Идентификатор {identifier} с ID '{identifier_hash}' добавлен в таблицу. Индекс: {index}")
# b.display()


while True:
    print("\n1. Поиск идентификатора")
    print("2. Добавление нового идентификатора")
    print("3. Сохранение и выход\n")

    choice = input("Выберите действие (введите номер): ")

    if choice == '1':
        
        search_key = input("Введите идентификатор для поиска: ")
        element_to_find = b.hash_function(search_key)
        result = b.search(b, element_to_find)

        if result:
            print(f"Идентификатор '{search_key}' найден в таблице.")
        else:
            print(f"Идентификатор '{search_key}' не найден в таблице.")
        
        
    elif choice == '2':
        
        new_identifier = input("Введите новый идентификатор для добавления: ")
        identifier_hash = b.hash_function(new_identifier)
        b.insert(identifier_hash)
        identifier_data.append(new_identifier)
        print(f"Идентификатор '{new_identifier}' добавлен в таблицу.")
        
        
        
        
    elif choice == '3':
        
        b.save_list_to_file(file_path, identifier_data)
        print("Таблица сохранена. Программа завершена.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")


