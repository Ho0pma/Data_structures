# # Динамический массив
# marks = [1, 2, 3, 4, 5]
#
# # Приближенно считается тоже дм, но правильно дм должен иметь один тип данных
# lst = [True, 1, 'two']
#
# # но на самом деле внутри этой структуры хранятся ссылки на объекты - те это дм
# # в  lst хранятся ссылки на объекты разного типа
#
# # длина массива
# len(lst)
# print(lst)
#
# # вставка в конце массива
# lst.append(6.7)
# print(lst)
#
# # вставка в произвольную точку в списке
# lst.insert(0, 'First')
#
# # получить элемент в списке
# print(lst[2])
#
# # объединение списков
# print(marks + lst)

# cities = [1, 'Пермь', 2, 3, 'Пермь']
# if 'Пермь' in cities:
#     index = cities.index('Пермь')
#     result = None
#     if index == len(cities) - 1:
#         result = 1
#     else:
#         result = 'n'
#     cities.pop(index)
#     print(result)

# -------------------------------------------------------------------------------------------------------------------- #
# пример односвязного списка
# динамическая структура данных, которая состоит из узлов, элемент которых хранит в себе
# ссылку на следующий

# ЧТО НУЖНО ДОДЕЛАТЬ
# сделать переменную tail
# Метод __str__ не будет работать корректно, если список пустой. Нужно добавить проверку на случай пустого списка.
# В методе __getitem__ необходимо добавить проверку на выход за границы списка.
# В методе insert необходимо добавить проверку на выход за границы списка.
# В методе __delitem__ также нужна проверка на выход за границы списка.
# нет изменение элемента в списке
# class LinkedList:
#     head = None  # изначально список пустой
#     length = 0   # длинна тоже
#
#     # класс для создания элементов (узлов)
#     class Node:
#         element = None   # то, что мы храним
#         next_node = None # ссылка на следующую ноду (узел)
#
#         # функция инициализации для создания узлов
#         def __init__(self, element, next_node=None):
#             # element - то, что мы сохраняем
#             # next_node по умолчанию None, тк в конце не может быть следующего элемента
#
#             # тут присваиваем значения, которые мы получили на входе
#             self.element = element
#             self.next_node = next_node
#
#
#     # добавление в конец списка (сейчас O(n))
#     def append(self, element):
#         # если первого элемента нет - создаем его путем создания эк класса Node:
#         if not self.head:
#             self.head = self.Node(element)
#             self.length += 1                # увеличиваем тк создан новый элемент
#             return element
#
#         # если какой-то элемент уже есть в списке:
#         # нужно пройтись по всем элементам
#         node = self.head            # начальная нода
#         while node.next_node:        # пока существует следующая нода
#             node = node.next_node   # увеличиваем ноду, пока она есть
#
#         # когда дойдем до конца, делаем следующую ноду - новой
#         node.next_node = self.Node(element)
#         self.length += 1
#         return element
#
#     def __str__(self):
#         # если вызвать print(эк) - вызовется эта функция
#         # тут будем сохранять все узлы в формате строки
#         line = '['
#         node = self.head
#         while node.next_node:
#             line += f'{str(node.element)}, '
#             node = node.next_node
#
#         line += f'{str(node.element)}]'
#
#         return line
#
#     # доступ к элементу O(n)
#     def __getitem__(self, item):
#         # будет вызываться если вызвать print(lst[index])
#         node = self.head
#         index = 0
#         while index < item:         # пока не дошли до нужно значения
#             node = node.next_node
#             index += 1
#
#         return node.element
#
#     def insert(self, key, value):
#         node = self.head
#         prev_node = self.head
#         index = 0
#
#         # случай если мы вставляем в начало списка О(1)
#         if key == 0:
#             old_head = self.head                              # делаем текущую ноду - старой
#             self.head = self.Node(value, next_node=old_head)  # и задаем, что новая голова - новая нода (ту, которую вставляем)
#             self.length += 1
#             return value
#
#         # вставка в середину (любое другое место кроме первого) O(n)
#         while index < key:          # находим нужный индекс
#             prev_node = node        # п
#             node = node.next_node
#             index += 1
#
#         prev_node.next_node = self.Node(value, next_node=node)
#         self.length += 1
#         return value
#
#     #  Удаление элемента. Нет обработки ошибки, если такого элемента нет.
#     def __delitem__(self, key):
#         # при вызове del lst[index] зайдет сюда
#
#         node = self.head
#         prev_node = self.head
#         index = 0
#
#         # удаление первого элемента О(1)
#         if key == 0:
#             old_head = self.head
#             self.head = self.head.next_node
#             self.length -= 1
#
#             del old_head
#             # return element  # чтобы вывести, что удаляем нужно перед этим сохранять удаляемый элемент (не реализовано)
#             # del игнорирует возвращаемое значение
#
#         # удаление любого кроме первого O(n)
#         while index < key:
#             prev_node = node
#             node = node.next_node
#             index += 1
#
#         prev_node.next_node = node.next_node
#         self.length -= 1
#
#         del node
#
#
# lst = LinkedList()          # создаем объект
# lst.append(4)               # добавляем элементы
# lst.append(2)
#
# lst.insert(1, 3) # вставляем по индексу
# del lst[2]                  # удаляем по индексу: __delitem__
#
#
# print(lst)                  # выводим сформированный список: __str__
# print(lst[0])               # выводим значение из листа по индексу: __getitem__
# print(lst.length)           # выводим физический размер

# -------------------------------------------------------------------------------------------------------------------- #
# двусвязный список

# class DblList:
#     head = None
#     tail = None
#     length = 0
#
#     class Node:
#         prev_node = None
#         next_node = None
#         element = None
#
#         def __init__(self, element, prev_node=None, next_node=None):
#             self.prev_node = prev_node
#             self.next_node = next_node
#             self.element = element
#
#     def append(self, element):
#         self.length += 1
#
#         if not self.head:
#             self.head = self.Node(element)
#             return element
#
#         elif not self.tail:
#             self.tail = self.Node(element, prev_node=self.head, next_node=None)
#             self.head.next_node = self.tail
#             return element
#         else:
#             node = self.Node(element, prev_node=self.tail, next_node=None)
#             self.tail.next_node = node
#             self.tail = node
#             return element
#
#     def __iter__(self):
#         node = self.head
#
#         while node:
#             yield node.element
#             node = node.next_node
#
#     def _del(self, index, reverse=False):
#         if reverse:
#             i = self.length - 1
#             node = self.tail
#
#             while i != index:
#                 node = node.prev_node
#                 i -= 1
#         else:
#             i = 0
#             node = self.head
#
#             while i < index:
#                 node = node.next_node
#                 i += 1
#
#         element = node.element
#         node.prev_node.next_node, node.next_node.prev_node = node.next_node, node.prev_node
#         del node
#         return element
#
#     def __delitem__(self, index):
#         if index < 0 or index >= self.length:
#             raise IndexError('Index out of range')
#
#         elif index == 0:
#             old_head = self.head
#             self.head = self.head.next_node
#             del old_head
#
#         elif index == self.length - 1:
#             old_tail = self.tail
#             self.tail = self.tail.prev_node
#             self.tail.next_node = None
#             del old_tail
#
#         elif index <= self.length // 2:
#             self._del(index, reverse=False)
#
#         else:
#             self._del(index, reverse=True)
#
#         self.length -= 1
#
#     def _insrt(self, index, value, reverse=False):
#         if reverse:
#             i = self.length - 1
#             node = self.tail
#
#             while i != index:
#                 node = node.prev_node
#                 i -= 1
#         else:
#             i = 0
#             node = self.head
#
#             while i < index:
#                 node = node.next_node
#                 i += 1
#
#         new_node = self.Node(value, node.prev_node, node)
#         node.prev_node.next_node, node.prev_node = new_node, new_node
#         return value
#
#     def insert(self, index, value):
#         if index < 0 or index >= self.length:
#             raise IndexError('Index out of range')
#
#         elif index == 0:
#             new_node = self.Node(value, None, self.head)
#             new_node.next_node, self.head = self.head, new_node
#
#         elif index == self.length - 1:
#             new_node = self.Node(value, self.tail.prev_node, self.tail)
#             new_node.next_node, self.tail.prev_node.next_node = self.tail, new_node
#
#         elif index <= self.length // 2:
#             self._insrt(index, value, reverse=False)
#
#         else:
#             self._insrt(index, value, reverse=True)
#
#         self.length += 1
#
# if __name__ == '__main__':
#     dblList = DblList()
#
#     dblList.append(1)
#     dblList.append(2)
#     dblList.append(3)
#     dblList.append(4)
#     dblList.append(5)
#
#     dblList.insert(4, 999)
#
#     # del dblList[0]
#     # del dblList[5]
#     print(dblList.length)
#
#     print([i for i in dblList])

# -------------------------------------------------------------------------------------------------------------------- #
# collections.deque

from collections import deque

# создание пустой очереди
# dq = deque()
# print(dq) # выведет: deque([])

# задать итерируемый объект + установить длину очереди в 5, если ее нет - очередь бесконечна
# внутрь deque можно поместить любой итерируемый объект
# dq = deque([1, 2, 3, 4, 5], maxlen=5)
#
# # что будет если добавить в такую очередь еще элемент?
# dq.append(6)
#
# # все элементы были сдвинуты
# print(dq) # выведет: deque([2, 3, 4, 5, 6], maxlen=5)
#
# # можно также вставить слева
# dq.appendleft(7)
#
# print(dq) # выведет: deque([7, 2, 3, 4, 5], maxlen=5)
#
# # удалить граничные элементы
# value1 = dq.pop()
# value2 = dq.popleft()
#
# print(dq) # выведет: deque([2, 3, 4], maxlen=5)
# print(value1, value2) # выведет: 5 7

# как отловить ошибку при удалении элемента из пустой очереди?
# dq = deque()
# try:
#     value = dq.pop()
#     print(value)
# except Exception as e:
#     print(e)
#
# # output: pop from an empty deque

# добавление нескольких значений в конец очереди
# dq = deque([1, 2, 3, 4, 5])
# dq.extend([6, 7, 8])
# dq.extendleft([0, -1, -2]) # добавляется слева направо
#
# print(dq) # output: deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

# # вставка в произвольную позицию в списке
# dq = deque([1, 2, 3, 4, 5])
# dq.insert(1, 999)
#
# # добавить на место предпоследнего
# dq.insert(-1, 555)
#
# # чтобы добавить в конец очередь - указать несуществующее положительное число
# dq.insert(9999999, 4444)
#
# # в начало
# dq.insert(-9999999, 777)
#
# print(dq) # output: deque([777, 1, 999, 2, 3, 4, 555, 5, 4444])

# # удалить элемент по значению (первый попавшийся). Если такого значения нет - ValuerError
# dq = deque([1, 2, 3, 4, 3, 5])
# dq.remove(3)
#
# print(dq) # output: deque([1, 2, 4, 3, 5]) # первая тройка съебалась

# очистка списка
# dq = deque([1, 2, 3, 4, 3, 5])
# dq.clear()
#
# print(dq) # output: deque([])

# # создать копию
# dq = deque([1, 2, 3, 4, 3, 5])
# dq2 = dq.copy()
#
# print(dq2) # output: deque([1, 2, 3, 4, 3, 5])

# -------------------------------------------------------------------------------------------------------------------- #
# реализация FIFO и LIFO на deque

# # FIFO или наоборот
# dq = deque([1, 2, 3, 4, 5])
# dq.appendleft(10) # добавление слева
# dq.pop() #  удаление справа
#
# print(dq) # output: deque([10, 1, 2, 3, 4])
#
# # LIFO или наоборот
# dq = deque([1, 2, 3, 4, 5])
# dq.append(10)
# dq.pop()
#
# print(dq) # output: deque([1, 2, 3, 4, 5])

# -------------------------------------------------------------------------------------------------------------------- #
# задача:
# Подвиг 4. Создайте пустую очередь с именем q как объект класса deque.
# Добавьте справа (в конец) очереди q последовательно данные lst_in, прочитанные из входного потока:
#
# lst_in = list(map(int, input().split()))
# Извлеките слева (с начала) очереди первые три элемента и выведите их в консоль
# в одну строчку через пробел в порядке считывания.

# from collections import deque
#
# lst_in = [1, 2, 3, 4, 5]
#
# # здесь продолжайте программу
# q = deque(lst_in)
# print(q)
# i = 0
# while i < 3:
#     print(q.popleft(), end=' ')
#     i += 1
#
# # цикл можно было реализовать вот так
# # print(*[q.popleft() for _ in range(3)])

# -------------------------------------------------------------------------------------------------------------------- #
# задача:
# Подвиг 5. Создайте очередь с именем q как объект класса deque и следующими начальными данными:
#
# lst_in = list(map(str.strip, input().split()))
# Данные в очереди q должны идти в том же порядке, что и в списке lst_in
# (это равносильно тому, что значения из списка lst_in добавляются в конец (справа) очереди q).
#
# Вставьте в очередь q элемент со строкой "run" в третью позицию (позиции отсчитываются с единицы).
# Удалите из этой очереди первый найденный элемент со строкой "edit".
#
# P.S. На экран ничего выводить не нужно, только сформировать очередь q по заданию подвига.

# lst_in = [1, 2, 3, 4, 5, 'edit']
# q = deque(lst_in)
# q.insert(2, 'run')
# q.remove('edit')

# -------------------------------------------------------------------------------------------------------------------- #
# задача:
# Подвиг 6. С помощью класса deque создайте объект очереди с именем fifo.
# Затем реализуйте в программе очередь типа FIFO, добавляя в нее новые элементы в начало (слева).
#
# Поместите по порядку следования значения из data в очередь fifo, прочитанные из входного потока:
#
# data = list(map(int, input().split()))
# Извлеките из очереди три объекта (три целых числа) и выведите их на экран в одну строчку
# через пробел в порядке извлечения.

# data = [1, 2, 3, 4, 5]
#
# fifo = deque()
# for i in data:
#     fifo.appendleft(i)
#
# print(*[fifo.pop() for _ in range(3)])

# -------------------------------------------------------------------------------------------------------------------- #
# Подвиг 7. С помощью класса deque создайте объект очереди с именем lifo. Затем реализуйте в программе очередь
# типа LIFO, добавляя в нее новые элементы в конец (справа).
#
# Поместите по порядку следования значения из data в очередь lifo,
# прочитанные из входного потока:
#
# data = list(map(int, input().split()))
# Извлеките из очереди три объекта (три целых числа) и выведите их на экран в одну строчку
# через пробел в порядке извлечения.

# data = [1, 2, 3, 4, 5]
# lifo = deque()
#
# for i in data:
#     lifo.append(i)
#
# print(*[lifo.pop() for _ in range(3)])

# -------------------------------------------------------------------------------------------------------------------- #
# Подвиг 8. С помощью класса deque создайте буфер с именем buff для приема информации (целых чисел)
# с максимальным размером в 10 элементов. Буфер должен быть реализован по принципу очереди FIFO,
# причем добавление новых данных должно осуществляться в начало очереди (слева),
# а извлечение - справа (с конца очереди).
#
# Поместите в этот буфер данные data, прочитанные из входного потока:
#
# data = list(map(int, input().split()))
# Извлеките из буфера три элемента (три числа) и выведите их в консоль в порядке считывания из буфера
# в одну строчку через пробел.

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# buff = deque(maxlen=10)
# buff.extendleft(data)
#
# print(*[buff.pop() for _ in range(3)])

# -------------------------------------------------------------------------------------------------------------------- #
# Подвиг 9. Вам в браузере нужно реализовать кнопку back (<, назад). Для этого решено воспользоваться
# очередью типа LIFO, которая бы хранила историю посещения страниц пользователем (история URL-адресов).
#
# Создайте вначале в программе объект с именем back_url класса deque,
# который бы содержал максимум 20 URL-адресов. Данные предполагается добавлять
# и извлекать с конца очереди (справа).
#
# Добавьте в очередь back_url по порядку URL-адреса, прочитанные из входного потока:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Извлеките один (первый) элемент из очереди и отобразите его в консоли.

# lst_in = [i for i in range(21)]
# back_url = deque(maxlen=20)
#
# back_url.extend(lst_in)
# print(*[back_url.pop() for _ in range(1)])

# -------------------------------------------------------------------------------------------------------------------- #
# Подвиг 10 (на повторение). Вам нужно реализовать очередь типа LIFO, используя динамический массив
# (как это мы делали ранее в этом курсе). Для этого вначале создается объект lifo как динамический массив.
# Затем, в конец этого массива последовательно добавьте числа, прочитанные из входного потока:
#
# data = list(map(int, input().split()))
# Извлеките (также с конца) два значения и выведите их в консоль в порядке их считывания
# в одну строчку через пробел.

data = [1, 2, 3, 4, 5]

lifo = []
lifo.extend(data)
print(*[lifo.pop() for i in range(2)])