# Домашнее задание по теме "Генераторы"
# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.


def all_variants(text):
    length = 1
    while length <= len(text):
        index = 0
        while index + length <= len(text):
            yield text[index:index + length]
            index += 1
        length += 1


a = all_variants('abc')

for i in a:
    print(i)
