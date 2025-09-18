def is_prime(n: int) -> bool:
    if n <= 1: 
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # check divisors of form 6k ± 1
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# quick tests
print(is_prime(2))    # True
print(is_prime(37))   # True
print(is_prime(100))  # False
