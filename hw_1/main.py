def power_numbers(*args:int)->list:
    return list(i**2 for i in args)
print(power_numbers(1, 2, 5, 7))
"""
функция, которая принимает N целых чисел,
и возвращает список квадратов этих чисел
"""
ODD = "odd"
EVEN = "even"
PRIME = "prime"
"""
функция, которая на вход принимает список из целых чисел,
и возвращает только чётные/нечётные/простые числа
(выбор производится передачей дополнительного аргумента)
"""
def is_prime(s):
    for i in range(2, s):
        if s % i == 0:
            return False
            break
    return True
def filter_numbers(list_number:list,filter_type:str)->list:
    if filter_type==ODD:
        return list(filter(lambda x: x % 2 != 0, list_number))
    elif filter_type==EVEN:
        return list(filter(lambda x: x % 2 == 0, list_number))
    elif filter_type==PRIME:
        return list(filter(is_prime,list_number))
    else:
        print(f'yout filter types = {filter_type} and it should be one of the "odd","even""prime"')
print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([2, 3, 4, 5,15,33,21,565,11,13], PRIME))
