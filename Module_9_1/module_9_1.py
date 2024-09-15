# Домашнее задание по теме "Введение в функциональное программирование"
# Цель: научиться обращаться к функциям, как к объекту и передавать их в
# другие функции для вызова.


def apply_all_func(num_list, *functions):
    results = {}
    
    for f in functions:
        results[f.__name__] = f(num_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, 5.9, 9.1], min, max, len, sum, sorted))
