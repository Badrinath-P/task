def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Get input from the user
num = int(input("Enter a number: "))
result = sum_of_digits(num)

print("Sum of digits:", result)
