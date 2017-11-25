# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

print(command1)
print(command2)

command1 = command1.split()
command1 = command1[-1].split(',')
command2 = command2.split()
command2 = command2[-1].split(',')

set1 = set(command1)
set2 = set(command2)

print('set1:',set1)
print('set2:',set2)

vlans = set1 & set2

print('vlans:',vlans)






