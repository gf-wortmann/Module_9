# Домашнее задание по теме "Декораторы"
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

def is_prime(func):
    def wrapper(*args):
        def is_simple(num):
            if num <= 2:
                return True
            else:
                for i in range(2, num - 1):
                    if not num % i:
                        return False
                return True
        
        res = func(*args)
        if is_simple(res):
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)
print(sum_three(1, 2, 9, 13)) # ой! оно ест больше трех!
print(sum_three(1, 2, 4))
