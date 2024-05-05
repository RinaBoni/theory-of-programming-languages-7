import rply

 
class Token(rply.Token):
    __match_args__ = ('name', 'value')                  # теперь case будет рассматривать значения, передаваемые при сравнивании в том порядке, в котором они записаны в  match_args
    

    def __init__(self, name, value, source_pos=None):   # инициализация экземпляра, с помощью конструктор родительского класса (rply)
        super().__init__(name, value, source_pos)

    def __str__(self) -> str:                           # преобразование объекта в строковое представление
        return f'({self.name}; {self.value})'           # возвращает форматированную строку, представляющую объект

    def __repr__(self):                                 # переопределение стандартного представления, чтобы вернуть то же самое, что и метод __str__
        return str(self)                                