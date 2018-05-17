from random import randint
import os

clear = lambda: os.system('cls') # очистка консоли

def again():
    
    print('Хотите сыграть еще раз?')
    print("1. Играть еще раз")
    print("2. Выход в главное меню\n")
    change = int(input())
    if change == 1:
        clear()
        game()
    elif change == 2:
        mainmenu()

def game():
    a = randint(0,9)
    b = randint(0,9)
    c = randint(0,9)
    d = randint(0,9)
    st0 = str(a) + str(b) + str(c) + str(d)
    print ('Число загадано! Введите 4х значное число: ')
    num = 0
    while True:
        num += 1
        print ('номер попытки: ', num)
        st = input(':')

        if len(st) != 4:
            print ('Доложно быть 4 цифры')
            continue

        # подготовить проверку
        ls = list(st)
        ls0 = list(st0)

        # сосчитать быков
        bulls = 0
        for j in range(4):
            if ls[j] == ls0[j]:
                bulls += 1;
                ls[j] = ' ';
                ls0[j] = '*';
        
        # выйти если угадали
        if bulls == 4:
            print ('Вы угдали!!!\n')
            again()
            break

        # сосчитать коров
        cown = 0
        for j in range(4):
            n = ls[j]
            for k in range(4):
                if n == ls0[k]:
                    cown += 1
                    ls0[k] = '*';
                    break
        
        # вывести число быков и коров
        print ('Быков: ', bulls)
        print ('коров: ', cown)
        

def mainmenu():
    mainm = 1
    while mainm:
        clear()
        print("Меню: ")
        print("1. Играть")
        print("2. Выход из игры")
        pick = int(input("Ваш выбор: "))
        if pick == 1:
            clear()
            game()
        elif pick == 2:
            exit(0)
    return

mainmenu()
