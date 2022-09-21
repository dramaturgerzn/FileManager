import os

def mkdir():
    nm_dir = input('Введите название директории: ')
    os.mkdir(nm_dir)

def rmdir():
    nm_dir = input('Введите название удаляемой директории: ')
    os.rmdir(nm_dir)

def cd():
    path = input("Введите путь к директории (если хотите подняться на уровень"
                 "выше, введите '..' : ")
    os.chdir(path)

def pwd():
    print(f'Текущая директория: {os.getcwd()}')

