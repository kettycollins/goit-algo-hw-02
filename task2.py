import collections

def is_palindrome(string):
    # Перетворити рядок до нижнього регістру та видалити пробіли
    string = string.lower().replace(" ", "")

    # Створити двосторонню чергу
    deque = collections.deque(string)

    # Порівнювати символи з обох кінців черги
    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False

    return True