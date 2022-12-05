#!/usr/bin/env python3
# coding=utf-8

# Имеется таблица в два столбца и 10 строк. В первом столбце исходные данные,
# во втором нужно выполнить расчет значений по формуле:
# y = (a*x^4+b*x^3)/(a^2-b^3)^3/Proizv(K(i))-(Sum(K(i)%2)
# Вычисления произвести используя классы.

import math


class MyClass(object):

    def __init__(self):
        self.values = []

    def add_value(self, value):
        self.values.append(value)

    def get_value(self, index):
        return self.values[index]

    def proizv(self, index):
        prod = 1
        for i in range(index):
            prod *= self.values[i]
        return prod

    def summ_nechet(self, index):
        summa = 0
        if index >= 0:
            for i in range(index):
                if self.values[i] % 2:
                    summa += self.values[i]
        return summa

    def solution(self, i, a, b, x):
        chisl = a * math.pow(x, 4) + b * math.pow(x, 3)
        znam = math.pow(a, 2) - math.pow(b, 3)
        drob_ib_cube = math.pow(chisl / znam, 3)
        return drob_ib_cube / self.proizv(i) - self.summ_nechet(i - 1)
