def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

def reverse_array(arr):
    return arr[::-1]

# Reversing a number
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)

# Reversing an array
arr = input("Enter an array (space-separated): ").split()
arr = [int(x) for x in arr]
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)
