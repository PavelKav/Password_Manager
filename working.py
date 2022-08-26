import sys
from main_gui_py import *

class PasswordManager:

    def __init__(self):
        self.password_file = None
        self.password_dict = {}

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, log_pass = line.split(':')
                self.password_dict[site] = log_pass.split(",")

    def add_password(self, site, login, password):
        self.password_dict[site] = login, password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                f.write(site + ':' + login + ',' + password + '\n')



def main():

    pm = PasswordManager()

    password_dict = {
        'vk': ['pavel', 'KAVERZIN'],
        'email': ['nizrevak3', 'io1uoihjasdfoihoui23h'],
        'pornhub':['мягкие_киски', 'Большие_сосиски']
    }

    #site = input('Введите название сайта : ')
    #login = input('Введите логин : ')
    #password = input('Введите пароль : ')





    print(""" Что ты хочешь сделать? 
       (1) Создать новый пароль
       (2) Показать сайт, логин, пароль
       (3) Показать значение словаря
       (4) Создать новый файл с паролями
       (5) Загрузить файл с паролями
       (Выйти)
       """)
    done = False

    while not done:

        choice = input('Выберите действие: ')
        if choice == '1':
            site = input('Введите название сайта : ')
            login = input('Введите логин : ')
            password = input('Введите пароль : ')
            pm.add_password(site, login, password)
        elif choice == '2':
            site = input("Введите сайт: ")
            login = pm.password_dict[site][0]
            password = pm.password_dict[site][1]
            print(f'Ваш логин - {login} , пароль - {password} ')
        elif choice == '3':
            print(f'Значение словаря password_dict = {pm.password_dict}')
        elif choice == '4':
            path = input('Введите название файла с паролями: ')
            pm.create_password_file(path)
        elif choice == '5':
            path = 'passtest.pass'#input('Введите название файла с паролями: ')
            pm.load_password_file(path)
        elif choice == "Выйти":
            done = True
            print("Пока")
        else:
            print("неверный выбор")




if __name__ == '__main__':
    main()
