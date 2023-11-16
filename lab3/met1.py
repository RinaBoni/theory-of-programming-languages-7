class Node:
    def __init__(self, key, identifier_id):
        self.key = key
        self.identifier_id = identifier_id
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def search(root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def build_tree(filename):
        root = None
        with open(filename, 'r') as file:
            for line in file:
                identifier = line.strip()[:32]  # Ограничиваем длину идентификатора 32 символами
                root = self.insert(root, identifier)
        return root

    def save_tree_to_file(root, filename):
        with open(filename, 'w') as file:
            if root:
                file.write(root.val + '\n')
                self.save_tree_to_file(root.left, filename)
                self.save_tree_to_file(root.right, filename)



def main():
    file_path = 'identifiers.txt'
    table_size = 32
    hash_table = HashTable(table_size)

    with open(file_path, 'r') as file:
        identifier_data = [line.split() for line in file.read().splitlines()]

    for index, (identifier, identifier_id) in enumerate(identifier_data, start=1):
        hash_table.insert(identifier, identifier_id)
        print(f"Идентификатор '{identifier}' с ID '{identifier_id}' добавлен в таблицу. Индекс: {index}")

    while True:
        print("\n1. Поиск идентификатора")
        print("2. Добавление нового идентификатора")
        print("3. Сохранение и выход")

        choice = input("Выберите действие (введите номер): ")

        if choice == '1':
            search_key = input("Введите идентификатор для поиска: ")
            result = hash_table.search(search_key)
            if result is not None:
                print(f"Идентификатор '{search_key}' с ID '{result}' найден в таблице.")
            else:
                print(f"Идентификатор '{search_key}' не найден в таблице.")
        elif choice == '2':
            new_identifier = input("Введите новый идентификатор для добавления: ")
            identifier_id = input("Введите ID для нового идентификатора: ")
            hash_table.insert(new_identifier, identifier_id)
            print(f"Идентификатор '{new_identifier}' с ID '{identifier_id}' добавлен в таблицу.")
        elif choice == '3':
            hash_table.save_to_file(file_path)
            print("Таблица сохранена. Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")

if __name__ == "__main__":
    main()
