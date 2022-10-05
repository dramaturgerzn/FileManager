import os
import shutil

upper_dir = os.getcwd()


def mkdir():
    path = input('Введите название новой директории, если хотите создать ее в текущем каталоге, или путь к ней: ')
    if (os.getcwd() == upper_dir) and not (upper_dir in path) and (path.count('\\') != 0 or path.count('/') != 0):
        print('Вы пытаетесь подняться выше рабочей директории.' + '\n')
    else:
        try:
            os.mkdir(path)
            print(f'Директория {path} создана.' + '\n')
        except FileExistsError:
            print('Создаваемая директория или файл уже существует.' + '\n')


def rmdir():
    path = input('Введите название или путь удаляемой директории: ')
    if (os.getcwd() == upper_dir) and not (upper_dir in path) and (path.count('`\`') != 0 or path.count('/') != 0):
        print('Вы пытаетесь подняться выше рабочей директории.' + '\n')
    else:
        try:
            os.rmdir(path)
            print(f'Директория {path} удалена.' + '\n')
        except FileNotFoundError:
            print('Удаляемая директория или файл не найден.' + '\n')


def cd():
    path = input("Введите путь к директории (если хотите подняться на уровень"
                 " выше, введите '..' : ")
    if path == '..' and os.getcwd() == upper_dir:
        print('Вы в домашней папке, нельзя подняться на уровень выше' + '\n')
    else:
        try:
            os.chdir(path)
        except FileNotFoundError:
            print('Путь не найден.' + '\n')


def pwd():
    print(f'Текущая директория: {os.getcwd()}' + '\n')


def cr_file():
    nm_file = input('Введите название нового файла С РАСШИРЕНИЕМ TXT (или путь к файлу): ')
    f = open(nm_file, 'w')
    f.close()
    print(f'Файл {nm_file} создан.' + '\n')


def wr_file():
    nm_file = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу), в который нужно записать текст: ')
    data = input('Введите текст для записи (запись осуществляется с новой строки), затем нажмите ENTER: ')
    f = open(nm_file, 'a')
    f.write(f"{data}" + '\n' + '\n')
    f.close()


def cat():
    nm_file = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для просмотра содержимого: ')
    try:
        f = open(nm_file, 'r')
        for line in f:
            print(line[:-1])
        f.close()
    except FileNotFoundError:
        print('Файл не найден.')


def rm_file():
    nm_file = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для удаления: ')
    try:
        os.remove(nm_file)
        print(f'Файл {nm_file} удален.' + '\n')
    except FileNotFoundError:
        print('Файл не найден.')


def rnm_file():
    old = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для переименнования: ')
    new = input('Введите новое название для переименнования: ')
    try:
        os.rename(old, new)
        print(f'Файл `{old}` перееименнован в `{new}`.' + '\n')
    except FileNotFoundError:
        print('Файл не найден.')


def mv_file():
    old = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для перемещения: ')
    new = input('Введите новый путь: ')
    try:
        shutil.move(old, new)
    except FileNotFoundError:
        print('Файл не найден.')


def copy_file():
    old = input('Введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для копирования: ')
    new = input('Введите новый путь: ')
    try:
        shutil.copy(old, new)
    except FileNotFoundError:
        print('Файл не найден.')


def menu():
    st = ''
    print('\n' + f'ВАША ДОМАШНЯЯ ДИРЕКТОРИЯ: {os.getcwd()}. НЕЛЬЗЯ ВЫХОДИТЬ ВЫШЕ ДОМАШНЕЙ ДИРЕКТОРИИ.' + '\n')
    while True:
        print('0. Вывести текущую рабочую директорию.')
        print('1. Создать папку.')
        print('2. Удалить папку.')
        print('3. Переместиться в другую папку или подняться на уровень выше.')
        print('4. Создание пустого файла.')
        print('5. Запись текста в файл.')
        print('6. Просмотр содержимого файла.')
        print('7. Удаление файла по имени.')
        print('8. Копирование файла.')
        print('9. Перемещение файла.')
        print('10. Переименование файла.')
        print('ВВЕДИТЕ EXIT ДЛЯ ЗАВЕРШЕНИЯ РАБОТЫ ПРОГРАММЫ.')
        st = input('ВЫБЕРИТЕ ДЕЙСТВИЕ: ')
        print('')

        if st == '0':
            pwd()

        elif st == '1':
            mkdir()

        elif st == '2':
            rmdir()

        elif st == '3':
            cd()

        elif st == '4':
            cr_file()

        elif st == '5':
            wr_file()

        elif st == '6':
            cat()

        elif st == '7':
            rm_file()

        elif st == '8':
            copy_file()

        elif st == '9':
            mv_file()

        elif st == '10':
            rnm_file()

        elif st.lower() == 'exit':
            print('Завершение работы программы...')
            break

        else:
            print('Вы выбрали несуществующий пункт меню, повторите ввод' + '\n')


menu()
