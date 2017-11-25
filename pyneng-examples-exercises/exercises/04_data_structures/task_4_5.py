# -*- coding: utf-8 -*-
'''
Задание 4.5

Список VLANS это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

print(type(VLANS),VLANS)

set_VLANS = set(VLANS)              #convert to set and deduplicate
print(type(set_VLANS), set_VLANS)

VLANS = list(set_VLANS)             #convert back to list
print(type(VLANS), VLANS)

sorted_VLANS = sorted(VLANS)        #sort list VLANS
print(sorted_VLANS)

