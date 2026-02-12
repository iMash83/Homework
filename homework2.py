import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка відповідності параметрів вимогам
    if not (1 <= min <= quantity <= max <= 1000):
        return []

    # Створення набору випадкових чисел у заданому діапазоні
    try:
        numbers = random.sample(range(min, max + 1), quantity)
    except ValueError:
        return []

    # Повернення відсортованого списку
    return sorted(numbers)

# Приклад 
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)