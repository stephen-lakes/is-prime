def is_prime(n:int) -> str:
    """
    checks if a given number is prime.
    """
    if n == 2 or n == 3:
        return True
    else:
        for num in range(2, (n//2) + 1):
            if n % num == 0:
                return False
        else:
            return True

print(is_prime(541))  # True
