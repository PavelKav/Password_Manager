from cryptography.fernet import Fernet


# region imported
# создаем класс PasswordManager
class PasswordManager:
    # инициализация класса
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    # функция создания файла генерированного ключа доступа к паролям
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    # функция загрузки сгенерированного ключа
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    # функция создания файла с паролями
    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    # функция загрузки файла с паролями
    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(':')
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode())

    # функция добавления пароля в файл с паролями
    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ':' + encrypted.decode() + '\n')

    #
    def get_password(self, site):
        return self.password_dict[site]


# endregion
def main():

    pm = PasswordManager()

    print(""" Что ты хочешь сделать? 
    (1) Создать новый ключ
    (2) Загрузить ключ
    (3) Создать новый файл с паролями
    (4) Загрузить файл с паролями
    (5) Добавить новый пароль
    (6) Показать пароль
    (выход)
    """)

    done = False

    while not done:

        choice = input('Выберите действие: ')
        if choice == '1':
            path = input('Выберите путь: ')
            pm.create_key(path)
        elif choice == '2':
            path = input('Выберите путь: ')
            pm.load_key(path)
        elif choice == '3':
            path = input("Выберите путь: ")
            pm.create_password_file(path)
        elif choice == '4':
            path = input("Выберите путь: ")
            pm.load_password_file(path)
        elif choice == '5':
            site = input("Введите название ресурса: ")
            password = input("Введите пароль: ")
            pm.add_password(site, password)
        elif choice == '6':
            site = input("Введите название ресурса, чтобы узнать пароль: ")
            print(f'Пароль для {site} - {pm.get_password(site)}')
        elif choice == "Выйти":
            done = True
            print("Пока")
        elif choice == '7':
            site = input("Введите название ресурса, чтобы узнать пароль: ")
            print(pm.password_dict.items())

        else:
            print("неверный выбор")


if __name__ == "__main__":
    main()
