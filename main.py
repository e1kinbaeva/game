
from example import generate_equation
import time


def operation():
    print("Добро пожаловать в игру 'Реши арифметические операции!'")
    name = input("Для начала давайте познакомимся. Введите ваше имя: ")
    time.sleep(1)
    print(f"\nРада знакомству {name}. Вы находитесь на первом уровне. \n")
    time.sleep(1)
    print(f"{name} Чтобы пройти первый уровень вы должны правильно решить 6 уравнений  и набрать 6 очков за 24 секунд. \n")
    time.sleep(4
               )
    print("За каждый правильный ответ вы получите одно очко. \n")
    time.sleep(1)
    print("Ну что ж  начнём? \n")
    time.sleep(3)
    print("3 ....")
    time.sleep(1)
    print("2 ....")
    time.sleep(1)
    print("1 ....")
    time.sleep(1)
    print("0 ....")


    point = 0

    start_time = time.time()
    end_time = start_time + 24
    attempts = 0

    while attempts < 6 and time.time() < end_time:
        equ, result = generate_equation()
        print(f"{name} решите уравнение: {equ} \n")
        print("Подсказка: если сложная задача, то вы можете пропустить нажав ENTER. \n")
        user_answer = input("Введите ваш ответ : ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Пожалуйста, введите целое число или 'exit'.")
            continue

        if user_answer == result:
            point += 1
            print("Правильно!")
        else:
            print(f"Неправильно. Правильный ответ: {result}")

        print(f"Ваш текущий счет: {point}\n")

    print(f"Игра окончена. Ваш итоговый счет: {point}")
    if point >= 6:
        print("Вы прошли первый уровень игры.")
    else:
        print(":( К сожалению вы не смогли пройти первый уровень, попробуйте пройти снова.")

operation()