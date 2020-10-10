import sys

class process():   # класс в которм происходит обработка данных

    alphabetBIG = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ'
    alphabetLITTLE = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
    new = str()   # Переменная, в которой собирается изменённая строка

    def __init__(self, name, count): # Передаём введённые пользователем данные в класс
        self.name = name
        self.shift = count

    def encode(self): # Кодирование данных (Если вводятся не русские буквы, то эти элементы пропускаются)
        for i in self.name:
            if i in process.alphabetBIG: # Ищем индекс, смещаем, записываем и выводим
                index = process.alphabetBIG.index(i)%len(process.alphabetBIG)
                process.new += process.alphabetBIG[(index + self.shift)%len(process.alphabetBIG)]
            elif i in process.alphabetLITTLE:
                index = process.alphabetLITTLE.index(i)%len(process.alphabetLITTLE)
                process.new += process.alphabetLITTLE[(index + self.shift)%len(process.alphabetLITTLE)]
            else:
                process.new = process.new + i
        print(process.new)
        process.new = '' # Обнуляем

    def decode(self): # Декодирование данных (Если вводятся не русские буквы, то эти элементы пропускаются)
        for i in self.name:
            if i in process.alphabetBIG: # Ищем индекс, смещаем, записываем и выводим
                index = process.alphabetBIG.index(i)%len(process.alphabetBIG)
                process.new += process.alphabetBIG[(index - self.shift)%len(process.alphabetBIG)]
            elif i in process.alphabetLITTLE:
                index = process.alphabetLITTLE.index(i)%len(process.alphabetLITTLE)
                process.new += process.alphabetLITTLE[(index - self.shift)%len(process.alphabetLITTLE)]
            else:
                process.new = process.new + i
        print(process.new)
        process.new = '' # Обнуляем



if __name__ == '__main__':
    while True: # Бесконечный цикл

        print('\n1 - encode\n'
              '2 - decode\n')

        command = input() # Выбирается режим работы

        if command == '1':
            print('Enter text')
            text = input()
            print('Enter count of shift')
            sh = int(input())
            proc = process(text,sh)
            proc.encode()

        if command == '2':
            print('Enter text')
            text = input()
            print('Enter count of shift')
            sh = int(input())
            proc = process(text,sh)
            proc.decode()

