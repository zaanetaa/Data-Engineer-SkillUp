# Masz listę liczb całkowitych. Twoim zadaniem jest napisanie funkcji w Pythonie, która
# znajdzie drugą największą liczbę na tej liście.
# Jeśli lista zawiera mniej niż dwa unikalne numery, funkcja powinna zwrócić None.
import random
lista = [random.randint(0, 9999) for x in range (10)]
print(sorted(lista))

def find_second_largest_number(lista):
    if len(lista) <2:
        return None
    unique_list=list(set(lista))
    if len(unique_list) <2:
        return None
    sort_list = sorted(unique_list)
    return sort_list[-2]


print(find_second_largest_number(lista))