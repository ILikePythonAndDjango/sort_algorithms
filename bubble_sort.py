# -*- coding: utf-8 -*-
from random import random

array = []

for element in range(7):
    array.append(int(random() * 10))
print(array)
i = 0
while i < len(array):
    j = 0
    while j < i:
        if array[i] < array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        j += 1
    i += 1
print(array)
