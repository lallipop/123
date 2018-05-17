import os
clear = lambda: os.system('cls') # очистка консоли

users = {0: ["kirill", "kir", "admin"]}
lenthusers = len(users)
filedatabase = "Base.txt"

def writedatabase():
    global users
    file = open(filedatabase, 'w')
    for i in range(lenthusers):
        file.write(str(i) + " " + users[i][0] + " " + users[i][1] + " " + users[i][2] + "\n")
    file.close()

def readdatabase():
    global lenthusers
    global users
    OpenFile = True
    try:
        file = open(filedatabase, 'r')
    except FileNotFoundError:
        OpenFile = False
    if OpenFile:
        file = open(filedatabase, 'r')
        for line in file:
            data = line
            data = data.split(' ')
            data[3] = data[3][0:-1]
            users[int(data[0])] = data[1:]
        lenthusers = len(users)
        file.close()
    else:
        writedatabase()
    return 
                               

def createusers(role = False):
    global users
    clear()
    print("Регистрация:")
    reg = 1
    defroles = "user"
    global lenthusers
    while reg:
        login = input("Придумайте логин: ")
        if not login:
            print("Логин не может быть пустым!")
            print('Пройдите регистрацию заново!')
            os.system('pause')
        reg = 0
        for i in range(lenthusers):
            if login == users[i][0]:
                print("Логин уже занят!")
                reg = 1
                break
    if len(login) != 0:             
        password = input("Введите пароль: ")
        if not password:
            print("Пароль не может быть пустым!")
            print('Пройдите регистрацию заново!')
            os.system('pause')
        if len(password) != 0:
            if role:
                print('Выбирете роль для пользователя')
                print("Роль:")
                print("1. Admin")
                print("2. User")
                pick = int(input("Выбирете роль: "))
                if pick == 1:
                    defroles = "admin"
                else:
                    defroles = "user"
            users[lenthusers] = [login, password, defroles]
            lenthusers = len(users)
            writedatabase()
            print("Регистрация прошла успешно!")
            os.system('pause')
            return

def allusers():
    global users
    clear()
    print("ID\t\tLogin\t\tPassword\t\tRole")
    for i in range(lenthusers):
        print(str(i)+"\t\t"+users[i][0]+"\t\t"+users[i][1]+"\t\t\t"+users[i][2])
    os.system('pause')
    return

def changelogin(id):
    global users
    clear()
    print("Смена логина:")
    chan = 1
    while chan:
        login = input("Придумайте новый логин: ")
        chan = 0
        for i in range(lenthusers):
            if login == users[i][0]:
                print("Логин уже занят!")
                chan = 1
                break
    users[id][0] = login
    writedatabase()
    print("Изменение логина прошло успешно!")
    os.system('pause')
    return

def changedpas(id):
    global users
    clear()
    print("Изменение пароля:")
    chanpas = 1
    while  chanpas:
        password = input("Введите свой старый пароль: ")
        if password == users[id][1]:
            print("Ваш старый пароль введен верно!")
            users[id][1] = input("Придумайте новый пароль: ")
            chanpas = 0
        else:
            print("Ваш старый пароль введен не правильно!")
            chanpas = 1
    writedatabase()
    print("Изменение прошло успешно!")
    os.system('pause')
    return

def resetpas():
    global users
    clear()
    standardPassword = "qwerty1"
    print("Сброс пароля у пользователя:")
    respas = 1
    while respas:
        id = int(input("Введите id пользователя: "))
        if id >= lenthusers:
            print("Такого пользователя не существует!")
            print("Введите другой id!")
            respas = 1
        else:
            users[id][1] = standardPassword
            print("Вы сбросили пароль у пользователя!("+users[id][0]+")")
            respas = 0
    writedatabase()
    os.system('pause')
    return

def changeroles():
    global users
    clear()
    print("Изменение роли пользователя:")
    chanr = 1
    while clear:
        id = int(input("Введите id пользователя: "))
        if id >= lenthusers:
            print("Такого пользователя не существует!")
            print("Введите другой id!")
            chanr = 1
        else:
            print("Выбирете роль:")
            print("1. Admin")
            print("2. User")
            pick = int(input("Выбирете роль: "))
            if pick == 1:
                defroles = "admin"
                users[id][2] = defroles
                print(users[id][0] + " стал " + users[id][2])
                break
            elif pick == 2:
                defroles = "user"
                users[id][2] = defroles
                print(users[id][0] + " стал " + users[id][2])
                break
    writedatabase()
    os.system('pause')
    return

def delusers(id):
    global users
    clear()
    global lenthusers
    print("Удаление аккаунта: ")
    if users[id][2] == 'admin':
        print('Аккаунт админа удалять нельзя, если хотите удалить аккаунт, то нужно изменить роль на пользователя!')
        os.system('pause')
        adminmod(id)
    elif users[id][2] != 'admin':
        while id + 1 < lenthusers:
            users[id][0] = users[id + 1][0]
            users[id][1] = users[id + 1][1]
            users[id][2] = users[id + 1][2]    
        users.pop(len(users) - 1)
        lenthusers = len(users)
        print("Вы успешно удалили аккаунт")
    writedatabase()
    os.system('pause')
    mainmenu()
    return


def adminmod(id):
    global users
    adminmod = 1
    usersid = id
    while adminmod:
        clear()
        print("Вы вошли как: "+users[usersid][0]+"")
        print("Ваша роль: "+users[usersid][2]+"")
        print("1. Cоздать пользователя")
        print("2. Изменить логин")
        print("3. Изменить пароль")
        print("4. Сбросить пароль у пользователя")
        print("5. Все пользователи")
        print("6. Изменить роль пользователя")
        print("7. Удалить аккаунт ")
        print("8. Выйти из аккаунта")
        print("9. Выход")
        pick = int(input("Ваш выбор: "))
        if pick == 1:
            createusers(True)
        elif pick == 2:
            changelogin(usersid)
        elif pick == 3:
            changedpas(usersid)
        elif pick == 4:
            resetpas()
        elif pick == 5:
            allusers()
        elif pick == 6:
            changeroles()
        elif pick == 7:
            delusers(usersid)
        elif pick == 8:
            adminmod = 0
        elif pick == 9:
            exit(0)

def usersmod(id):
    global users
    usersmod = 1
    usersid = id
    while usersmod:
        clear()
        print("Вы вошли как: "+users[usersid][0]+"")
        print("Ваша роль: "+users[usersid][2]+"")
        print("1. Изменить логин")
        print("2. Изменить пароль")
        print("3. Удалить аккаунт")
        print("4. Выйти из аккаунта")
        print("5. Выход")
        pick = int(input("Ваш выбор: "))
        if pick == 1:
            changelogin(usersid)
        elif pick == 2:
            changedpas(usersid)
        elif pick == 3:
            delusers(usersid)
        elif pick == 4:
            usersmod = 0
        elif pick == 5:
            exit(0)

def sigin():
    global users
    clear()
    print("Вход в аккаунт:")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for i in range(lenthusers):
        if len(password) == 0:
            print('Ваш пароль не существует')
            os.system('pause')
            mainmenu()
        if (login == users[i][0]) and (password == users[i][1]):
            print("Вы вошли в аккаунт!")
            if users[i][2] == "admin":
                adminmod(i)
            elif users[i][2] == "":
                print('У вас нет роли, попроситие админа исправить эту ситуацию!')
                os.system('pause')
                mainmenu()
            else:
                usersmod(i)
            return
    print("Вы ввели неправильный логин или пароль")
    os.system('pause')
    return

def mainmenu():
    readdatabase()
    mainm = 1
    while mainm:
        clear()
        print("Меню: ")
        print("1. Войти")
        print("2. Регистрация")
        print("3. Выход")
        pick = int(input("Ваш выбор: "))
        if pick == 1:
            sigin()
        elif pick == 2:
            createusers()
        elif pick == 3:
            mainm = 0
    return

mainmenu()
