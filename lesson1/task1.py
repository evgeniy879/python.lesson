login = 'testlogin'
password = 1111
secret_word = 'testsecret'
print(login)
print(1234567890)
print(secret_word)

client_login = input('введите ваш логин ')
if login == client_login:
    print('корректный логин')
print()
client_password = int(input('введите пароль '))
if login != client_login:
    print('неверный логин')
if password == client_password:
    print('верный пароль')
if password != client_password:
    print('неверный пароль, если забыли, то введите кодовое слово')
    key_word = input('хотите ввести кодовое слово? да/нет ')
    if key_word == 'да':
        client_secret_word = input('введите кодовое слово ')
        if secret_word == client_secret_word:
            print("кодовые слова совпадают")
        else:
            print('слова не совпадают')
    if key_word == 'нет':
        client_secret_word = int(input('введите пароль '))
        if password == client_secret_word:
            print('верный пароль')
        if password != client_secret_word:
            print('неверный пароль')
