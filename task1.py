import queue

# Створити чергу заявок
queue = queue.Queue()

# Функція генерування заявки
def generate_request():
    # Створити нову заявку
    request = {}

    # Додати заявку до черги
    queue.put(request)

# Функція обробки заявки
def process_request():
    # Якщо черга не пуста
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()

        # Обробити заявку
        print(f"Обробляю заявку.")

    # Інакше
    else:
        # Вивести повідомлення, що черга пуста
        print("Черга пуста")

# Головний цикл програми
while True:
    #Поки користувач не вийде з програми:
    if input("Введіть 'q', щоб вийти: ") == "q":
        break
    
    else:
        # Виконати generate_request() для створення нових заявок
        generate_request()
        # Виконати process_request() для обробки заявок
        process_request()
