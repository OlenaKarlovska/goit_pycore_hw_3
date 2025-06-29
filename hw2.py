import random

def get_numbers_tickets(min=1, max=49, quantity=6):
    if min < 1 or max > 49 or quantity > max - min + 1:
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted (numbers)

lottery_numbers = get_numbers_tickets(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)