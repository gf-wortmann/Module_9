# Домашнее задание по теме "Итераторы"
# Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__.
# Закрепить навык создания и выбрасывания исключений.

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=None):
        if step is None:
            step = 1
        if step == 0:
            raise StepValueError
        else:
            self.pointer, self.start, self.stop, self.step = start, start, stop, step
    
    def __iter__(self):
        self.pointer = self.start
        return self
    
    def __next__(self):
        pointer = self.pointer
        if pointer > self.stop and self.step > 0:
            raise StopIteration
        elif pointer < self.stop and self.step < 0:
            raise StopIteration
        else:
            self.pointer += self.step
            return pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()


