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

    def search(self, key):
        index = self.hash_function(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].identifier_id
            index = (index + 1) % self.size
            if index == initial_index:
                break
        return None

    def insert(self, key, identifier_id):
        index = self.hash_function(key)
        initial_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == initial_index:
                # Хэш-таблица заполнена, вы можете добавить обработку этой ситуации по вашему усмотрению
                raise ValueError("Хэш-таблица заполнена")
        self.table[index] = Node(key, identifier_id)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            for node in self.table:
                if node is not None:
                    file.write(f"{node.key} {node.identifier_id}\n")

def main():
    file_path = 'identifiers2.txt'
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
