def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(num1, den1, num2, den2):
    # Find the least common multiple (LCM) of the denominators
    lcm = (den1 * den2) // gcd(den1, den2)
    
    # Convert both fractions to have a common denominator
    num1 *= lcm // den1
    num2 *= lcm // den2
    
    # Add the numerators
    sum_num = num1 + num2
    
    # Find the greatest common divisor (GCD) of the numerator and denominator of the sum
    common_gcd = gcd(sum_num, lcm)
    
    # Simplify the fraction by dividing both the numerator and denominator by the GCD
    result_num = sum_num // common_gcd
    result_den = lcm // common_gcd
    
    return result_num, result_den

# Get input from the user
numerator1 = int(input("Enter the numerator of the first fraction: "))
denominator1 = int(input("Enter the denominator of the first fraction: "))
numerator2 = int(input("Enter the numerator of the second fraction: "))
denominator2 = int(input("Enter the denominator of the second fraction: "))

# Add the fractions
result_numerator, result_denominator = add_fractions(numerator1, denominator1, numerator2, denominator2)

# Display the result
print(f"The sum of the fractions is: {result_numerator}/{result_denominator}")
