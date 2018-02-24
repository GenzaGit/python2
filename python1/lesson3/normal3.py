#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

name = ['John', 'Vlad', 'Alex', 'Sam']
salary = [35000, 100000, 120000, 41000]
result = dict(zip(name, salary))
with open('salary.txt', 'w') as file:
    for index, val in result.items():
        file.write(index + ' - ' + str(val) + '\n')

with open('salary.txt', 'r') as file:
    for line in file:
        sal = int(line.split(' - ')[1].strip()) * 0.87
        print(line.split(' - ')[0].upper(), str(sal))

print('Не более 50000 получают: ', str(list(filter(lambda x: list(x)[1] < 50000, result.items()))).upper())