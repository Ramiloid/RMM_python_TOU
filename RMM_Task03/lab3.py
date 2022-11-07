#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если во втором столбце стоят две единицы, то уменьшить макс. элемент первой
# строки в два раза, а все единицы в таблице заменить нулями.

import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
print('Подсчитать количество отрицательных элементов в таблице и увеличить на это значение минимальный и максимальный элементы таблицы')

def random_array(n, m, max_value=20):
    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 19 и добавляем его в подмассив
            number = random.randint(-max_value, max_value)
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию
        print()  # переход на новую строку

def findNegative(array):
    negativeNumber = 0
    for i in array:
        for j in i:
            if(j<0):
                negativeNumber+=1
    print("Count of negative number is " + str(negativeNumber))
    return negativeNumber

def findMaxMinDoTask(array,negativeNumber):
    maxValue = 0
    minValue = 0
    for i in array:
        for j in i:
            if (j > maxValue):
                maxValue = j
            if(j < minValue):
                minValue = j
    for index, i in enumerate(array):
        for jindex, j in enumerate(i):
            if(j == maxValue):
                array[index][jindex] = j + negativeNumber
    for index, i in enumerate(array):
        for jindex, j in enumerate(i):
            if (j == minValue):
                array[index][jindex] = j + negativeNumber
    return array




def main():
    array = random_array(4, 5)  # заполняем массив случайными числами
    print_array(array)  # выводим массив на экран
    # Бесконечный цикл while, который закончится только при помощи break
    while True:
        print  # переход на новую строку
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        # Получаем ввод команды от пользователя
        key = input('Введите команду (1, 2 или 3): ')

        ########################################################################################

        if key == '1':  # если команда 1, то заполняем массив заново
            array = random_array(4, 5)
            print_array(array)
            # После этого условия цикл начнется с начала

        #########################################################################################

        elif key == '2':  # если команда 2, то проверяем условие
            print()  # переход на новую строку
            negativeNumbersCount = findNegative(array)
            array = findMaxMinDoTask(array,negativeNumbersCount)
                # Выводим на экран результаты
            print_array(array)
            break  # выход из цикла

        #########################################################################################

        elif key == '3':
            exit(0)  # выходим из программы


if __name__ == '__main__':
    main()
