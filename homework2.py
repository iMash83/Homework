import random

def get_numbers_ticket(min_val, max_val, quantity):
 
    if not (1 <= min_val <= quantity <= max_val <= 1000):
        return []

    numbers_range = range(min_val, max_val + 1)
    lucky_numbers = random.sample(numbers_range, quantity)
    
    return sorted(lucky_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)