import sys

class process():

    alphabetBIG = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ'
    alphabetLITTLE = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
    new = str()

    def __init__(self, name, count):
        self.name = name
        self.shift = count

    def encode(self):
        for i in self.name:
            if i in process.alphabetBIG:
                index = process.alphabetBIG.index(i)%len(process.alphabetBIG)
                process.new += process.alphabetBIG[(index + self.shift)%len(process.alphabetBIG)]
            elif i in process.alphabetLITTLE:
                index = process.alphabetLITTLE.index(i)%len(process.alphabetLITTLE)
                process.new +=  process.alphabetLITTLE[(index + self.shift)%len(process.alphabetLITTLE)]
            else:
                process.new = process.new + i
        print(process.new)
        process.new = ''

    def decode(self):
        for i in self.name:
            if i in process.alphabetBIG:
                index = process.alphabetBIG.index(i)%len(process.alphabetBIG)
                process.new += process.alphabetBIG[(index - self.shift)%len(process.alphabetBIG)]
            elif i in process.alphabetLITTLE:
                index = process.alphabetLITTLE.index(i)%len(process.alphabetLITTLE)
                process.new +=  process.alphabetLITTLE[(index - self.shift)%len(process.alphabetLITTLE)]
            else:
                process.new = process.new + i
        print(process.new)
        process.new = ''



if __name__ == '__main__':
    while True:

        print('\n1 - encode\n'
              '2 - decode\n')

        command = input()

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

