"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

def guess_number(num, tries):
    guess = int(input("Угадайте число от 0 до 100: "))
    if guess == num:
        print("Поздравляю, вы угадали число!")
    elif tries == 1:
        print("К сожалению, вы не угадали число. Было загадано число", num)
    else:
        if guess < num:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
        guess_number(num, tries - 1)

secret_number = random.randint(0, 100)

print("У вас есть 10 попыток, чтобы угадать число от 0 до 100.")
guess_number(secret_number, 10)
