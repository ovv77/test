# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

input_list = ospf_route.split()

DictProtocol = {'O':'OSPF',                # Dict for protocols
                'B':'BGP',
                'R':'RIP'
                }

cols = '''{:20} {:15}'''
print(cols.format('Protocol', DictProtocol.get(input_list[0]))) # вытаскиваем ключ из строки и получаем значение из словаря
print(cols.format('Prefix', input_list[1]))
print(cols.format('AD/metric', str(input_list[2]).strip('[]')))
print(cols.format('Next-Hop', input_list[4]))
print(cols.format('Last update', input_list[5]))
print(cols.format('Outbound Interface', input_list[6]))