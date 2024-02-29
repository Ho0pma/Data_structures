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

# пример односвязного списка
# динамическая структура данных, которая состоит из узлов, элемент которых хранит в себе
# ссылку на следующий

# ЧТО НУЖНО ДОДЕЛАТЬ
# Метод __str__ не будет работать корректно, если список пустой. Нужно добавить проверку на случай пустого списка.
# В методе __getitem__ необходимо добавить проверку на выход за границы списка.
# В методе insert необходимо добавить проверку на выход за границы списка.
# В методе __delitem__ также нужна проверка на выход за границы списка.
class LinkedList:
    head = None  # изначально список пустой
    length = 0   # длинна тоже

    # класс для создания элементов (узлов)
    class Node:
        element = None   # то, что мы храним
        next_node = None # ссылка на следующую ноду (узел)

        # функция инициализации для создания узлов
        def __init__(self, element, next_node=None):
            # element - то, что мы сохраняем
            # next_node по умолчанию None, тк в конце не может быть следующего элемента

            # тут присваиваем значения, которые мы получили на входе
            self.element = element
            self.next_node = next_node


    # добавление в конец списка (сейчас O(n))
    def append(self, element):
        # если первого элемента нет - создаем его путем создания эк класса Node:
        if not self.head:
            self.head = self.Node(element)
            self.length += 1                # увеличиваем тк создан новый элемент
            return element

        # если какой-то элемент уже есть в списке:
        # нужно пройтись по всем элементам
        node = self.head            # начальная нода
        while node.next_node:        # пока существует следующая нода
            node = node.next_node   # увеличиваем ноду, пока она есть

        # когда дойдем до конца, делаем следующую ноду - новой
        node.next_node = self.Node(element)
        self.length += 1
        return element

    def __str__(self):
        # если вызвать print(эк) - вызовется эта функция
        # тут будем сохранять все узлы в формате строки
        line = '['
        node = self.head
        while node.next_node:
            line += f'{str(node.element)}, '
            node = node.next_node

        line += f'{str(node.element)}]'

        return line

    # доступ к элементу O(n)
    def __getitem__(self, item):
        # будет вызываться если вызвать print(lst[index])
        node = self.head
        index = 0
        while index < item:         # пока не дошли до нужно значения
            node = node.next_node
            index += 1

        return node.element

    def insert(self, key, value):
        node = self.head
        prev_node = self.head
        index = 0

        # случай если мы вставляем в начало списка О(1)
        if key == 0:
            old_head = self.head                              # делаем текущую ноду - старой
            self.head = self.Node(value, next_node=old_head)  # и задаем, что новая голова - новая нода (ту, которую вставляем)
            self.length += 1
            return value

        # вставка в середину (любое другое место кроме первого) O(n)
        while index < key:          # находим нужный индекс
            prev_node = node        # п
            node = node.next_node
            index += 1

        prev_node.next_node = self.Node(value, next_node=node)
        self.length += 1
        return value

    #  Удаление элемента. Нет обработки ошибки, если такого элемента нет.
    def __delitem__(self, key):
        # при вызове del lst[index] зайдет сюда

        node = self.head
        prev_node = self.head
        index = 0

        # удаление первого элемента О(1)
        if key == 0:
            old_head = self.head
            self.head = self.head.next_node
            self.length -= 1

            del old_head
            # return element  # чтобы вывести, что удаляем нужно перед этим сохранять удаляемый элемент (не реализовано)
            # del игнорирует возвращаемое значение

        # удаление любого кроме первого O(n)
        while index < key:
            prev_node = node
            node = node.next_node
            index += 1

        prev_node.next_node = node.next_node
        self.length -= 1

        del node


lst = LinkedList()          # создаем объект
lst.append(4)               # добавляем элементы
lst.append(2)

lst.insert(1, 3) # вставляем по индексу
del lst[2]                  # удаляем по индексу: __delitem__


print(lst)                  # выводим сформированный список: __str__
print(lst[0])               # выводим значение из листа по индексу: __getitem__
print(lst.length)           # выводим физический размер

























