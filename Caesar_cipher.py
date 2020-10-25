import sys
import logging

class process():   # класс в которм происходит обработка данных

    alphabetBIG = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ'
    alphabetLITTLE = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
    new = str()   # Переменная, в которой собирается изменённая строка

    def __init__(self, name, count): # Передаём введённые пользователем данные в локальные переменные
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
        new_n = process.new
        process.new = ''
        return (new_n)


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
        new_n = process.new
        process.new = ''
        return (new_n)


if __name__ == '__main__':
    logging.basicConfig(filename='С_s.log', filemode='a', format='%(asctime)s  :  %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('User started working')
    while True: # Бесконечный цикл

        print('\nОбрабатываются только русские буквы, остальные символы пропускаются.\n'
              '1 - encode\n'
              '2 - decode\n')
        command = input() # Выбирается режим работы
        logging.info('User selected the operating mode - ' + str(command))

        if command == '1':
            print('Enter text')
            text = input()
            logging.info('User added the text - ' + text)
            print('Enter count of shift')
            try:
                sh = int(input())
                logging.info('User added the shift - ' + str(sh))
                proc = process(text, sh)
                f = proc.encode()
                print(f)
                logging.info('End of operation - ' + f)
            except ValueError as e:
                logging.exception("Exception occurred")


        if command == '2':
            print('Enter text')
            text = input()
            logging.info('User added the text - ' + text)
            print('Enter count of shift')
            try:
                sh = int(input())
                logging.info('User added the shift - ' + str(sh))
                proc = process(text, sh)
                f = proc.decode()
                print(f)
                logging.info('End of operation - ' + f)
            except ValueError as e:
                logging.exception("Exception occurred")


        if command == '':
            logging.info('User stoped to working')
            break