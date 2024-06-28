import random
import time
import os

print("\n Цель игры: не взять последнюю палочку")
print(" За ход из общего кол-ва палочек можно удалить от 1-ой до 3-х\n")

while True:  # Ввод кол-ва палочек
    try:
        sticks_number = int(input(" Введите кол-во палочек для игры: "))
        break
    except:
        print(" Необходимо целое число")


lottery = [True, False]
print(" Кто же будет ходить?")
time.sleep(3)
move = random.choice(lottery)  # Флажок, определяющий очередность хода
def clear(): return os.system('cls')  # Очистка консоли
clear()


def player_move(del_sticks):  # Функция, реализующая ход игрока
    global sticks_number
    global move
    sticks_number -= del_sticks
    time.sleep(2)
    print(" Вы сделали свой ход")
    move = False
    print(f" Осталось палочек: {sticks_number}")
    time.sleep(5)
    clear()


def ai_move():  # Функция, реализующая ход компьютера
    global sticks_number
    global move
    print("\n Ходит ИИ!")
    if sticks_number > 4:
        if (sticks_number - 3) % 4 == 0 or (sticks_number - 2) % 4 == 0 \
                or (sticks_number - 1) % 4 == 0:
            if (sticks_number - 3) % 4 == 0:
                del_sticks = random.choice([1, 2])
            elif (sticks_number - 2) % 4 == 0:
                del_sticks = random.choice([1, 3])
            elif (sticks_number - 1) % 4 == 0:
                del_sticks = random.choice([2, 3])
        else:
            del_sticks = random.randint(1, 3)
    elif sticks_number == 4:
        del_sticks = 3
    elif sticks_number == 3:
        del_sticks = 2
    elif sticks_number <= 2:
        del_sticks = 1
    sticks_number -= del_sticks
    time.sleep(2)
    print(" ИИ сделал свой ход")
    move = True
    print(f" Осталось палочек: {sticks_number}")
    time.sleep(5)
    clear()


def correct_input():  # Безопасный ввод
    while True:
        try:
            del_sticks = int(input(" Сколько палочек удалить: "))
            break
        except:
            print(" Необходимо целое число")
    return del_sticks


# Eсли игрок вводит некорректное число, то ему приходится повторить свой выбор
def input_check(del_sticks):
    global sticks_number
    if sticks_number > 2:
        while del_sticks > 3 or del_sticks < 1:
            print(" Введите адекватное кол-во палочек(1-3)")
            del_sticks = correct_input()
        if 1 <= del_sticks <= 3:
            player_move(del_sticks)

    elif sticks_number == 2:
        while del_sticks > 2 or del_sticks < 1:
            print(" Введите адекватное кол-во палочек(1-2)")
            del_sticks = correct_input()
        if 1 <= del_sticks <= 2:
            player_move(del_sticks)

    elif sticks_number == 1:
        while del_sticks != 1:
            print(" Берите свою палочку, признайте поражение")
            del_sticks = correct_input()
        if del_sticks == 1:
            player_move(del_sticks)


while sticks_number > 0:  # Игра, поочередная смена ходов
    if move == True:
        print("\n Вы ходите!")
        print(f" Кол-во палочек: {sticks_number}")
        del_sticks = correct_input()
        if sticks_number > 2:
            if 1 <= del_sticks <= 3:
                player_move(del_sticks)
            else:
                input_check(del_sticks)
        elif sticks_number == 2:
            if 1 <= del_sticks <= 2:
                player_move(del_sticks)
            else:
                input_check(del_sticks)
        elif sticks_number == 1:
            if del_sticks == 1:
                player_move(del_sticks)
            else:
                input_check(del_sticks)
    elif move == False:
        ai_move()

if move == True:  # Флажок меняется после хода, на чьём ходе закончились палочки, тот проиграл
    print(" Вы победили!!!")
else:
    print(" Вы проиграли, т.к. взяли последнюю палочку")
