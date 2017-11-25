# -*- coding: utf-8 -*-

'''
Задание 19.2b

Переделать функцию send_config_commands из задания 19.2a или 19.2

Добавить проверку на ошибки:
* При выполнении команд, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр output также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками


Оба словаря в формате
* ключ - IP устройства
* значение -  вложенный словарь:
   * ключ - команда
   * значение - вывод с выполнением команд

Проверить функцию на команде с ошибкой.
'''
