# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.split(':')

print(type(MAC),MAC)

a = int(MAC[0],16)
print(a)


print("{:b} {:b} {:b}".format( int(MAC[0],16),int(MAC[1],16),int(MAC[2],16)))

