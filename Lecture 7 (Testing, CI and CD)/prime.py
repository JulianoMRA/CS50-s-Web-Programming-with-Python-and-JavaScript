import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % 1 == 0:
            return False
    return True
