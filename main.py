import os
import shutil


def mkdir():
    nm_dir = input('Введите название новой директории: ')
    os.mkdir(nm_dir)
    print(f'Директория {nm_dir} создана.')


def rmdir():
    nm_dir = input('Введите название удаляемой директории: ')
    os.rmdir(nm_dir)
    print(f'Директория {nm_dir} удалена.')


def cd():
    path = input("Введите путь к директории (если хотите подняться на уровень"
                 " выше, введите '..' : ")
    os.chdir(path)


def pwd():
    print(f'Текущая директория: {os.getcwd()}')


def cr_file():
    nm_file = input('Введите название нового файла С РАСШИРЕНИЕМ TXT (или путь к файлу): ')
    f = open(nm_file, 'w')
    f.close()
    print(f'Файл {nm_file} создан.')


def wr_file():
    nm_file = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу), в который нужно записать текст: ')
    data = input('Введите текст для записи (запись осуществляется с новой строки), затем нажмите ENTER: ')
    f = open(nm_file, 'a')
    f.write(f"{data}" + '\n')
    f.close()


def cat():
    nm_file = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для просмотра содержимого: ')
    f = open(nm_file, 'r')
    for line in f:
        print(line[:-1])
    f.close()


def rm_file():
    nm_file = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для удаления: ')
    os.remove(nm_file)
    print(f'Файл {nm_file} удален.')


def rnm_file():
    old = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для переименнования: ')
    new = input('Введите новое название для переименнования: ')
    os.rename(old, new)
    print(f'Файл `{old}` перееименнован в `{new}`.')


def mv_file():
    old = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для перемещения: ')
    new = input('Введите новый путь: ')
    shutil.move(old, new)


def copy_file():
    old = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для копирования: ')
    new = input('Введите новый путь: ')
    shutil.copy(old, new)


def menu():
    pass



