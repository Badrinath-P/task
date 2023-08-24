def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def reverse_digits(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def prime_with_twist(m):
    if is_prime(m) or is_prime(reverse_digits(m)):
        return True
    return False

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

if prime_with_twist(m):
    print(f"{m} is a prime with twist!")
else:
    print(f"{m} is not a prime with twist.")
