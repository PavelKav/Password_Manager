def main():
    pass


password_dict = {}


def load_password_file(path):
    password_file = path

    with open(path, 'r') as f:
        for line in f:
            site, log_pass = line.split(':')
            password_dict[site] = log_pass.split(',')



load_password_file('passtest.pass')

login = password_dict['vk'][0]
password = password_dict['vk'][1]

print(password_dict.keys())
print(password_dict.values())

print(f'логин - {login}')
print(f'пароль - {password}')

if __name__ == '__main__':
    main()
