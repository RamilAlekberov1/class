class Human:
    def __init__(self, n, a, h):
        print('Создан объект класса Human')
        self.name = n
        self.age = a
        self.height = h
        
    def print(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Рост: {self.height}')
        print('-'*30)
        
    def setData(self, n, a, h):
        self.name = n
        self.age = a
        self.height = h
        
person1 = Human('Рамиль', 17, 176)
person1.print()
   
person2 = Human('Костя', 17, 176)
person2.print()