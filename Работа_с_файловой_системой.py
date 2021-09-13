"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
Пример входного файла:
ab
c
dde
ff
﻿Пример выходного файла:
ff
dde
c
ab
"""

with open('dataset_24465_4.txt') as file1:
    f1_strings = f1.read().splitlines()

with open('result.txt', 'w') as file2:
    for line in f1_strings[::-1]:
        file2.write('%s\n' % line)
