
def main():

    password_dict = {
        'vk': ['pavel', 'KAVERZIN'],
        'email': ['nizrevak3', 'io1uoihjasdfoihoui23h'],
        'pornhub':['мягкие_киски', 'Большие_сосиски']
    }

    #site = input('Введите название сайта : ')
    #login = input('Введите логин : ')
    #password = input('Введите пароль : ')

    def add_password(site, login, password):
        password_dict[site] = login, password
        return password_dict



    print(""" Что ты хочешь сделать? 
       (1) Создать новый пароль
       (2) Показать сайт, логин, пароль
       (3) Показать значение словаря
       (Выйти)
       """)
    done = False

    while not done:

        choice = input('Выберите действие: ')
        if choice == '1':
            site = input('Введите название сайта : ')
            login = input('Введите логин : ')
            password = input('Введите пароль : ')
            add_password(site, login, password)
        elif choice == '2':
            site = input("Введите сайт: ")
            login = password_dict[site][0]
            password = password_dict[site][1]
            #print(f'Значение переменной site = {site}')
            #print(f'Значение переменной login = {login}')
            #print(f'Значение переменной password = {password}')
            print(f'Ваш логин - {login} , пароль - {password} ')
        elif choice == '3':
            print(f'Значение словаря password_dict = {password_dict}')
        elif choice == "Выйти":
            done = True
            print("Пока")
        else:
            print("неверный выбор")


    #print(f'Значение переменной site = {site}')
    #print(f'Значение переменной login = {login}')
    #print(f'Значение переменной password = {password}')
    #print(f'Значение словаря password_dict = {password_dict}')


    #print(f'Ваш логин - {login} , пароль - {password} ')


if __name__ == '__main__':
    main()
