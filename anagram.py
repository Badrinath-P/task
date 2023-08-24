def is_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are the same
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries to store character frequencies
    char_count_str1 = {}
    char_count_str2 = {}
    
    # Count the characters in the first string
    for char in str1:
        char_count_str1[char] = char_count_str1.get(char, 0) + 1
    
    # Count the characters in the second string
    for char in str2:
        char_count_str2[char] = char_count_str2.get(char, 0) + 1
    
    # Compare the character frequencies
    return char_count_str1 == char_count_str2

# Input strings
n = input("Enter the first string: ")
m = input("Enter the second string: ")

# Check if m is an anagram of n
if is_anagram(n, m):
    print(f"{m} is an anagram of {n}.")
else:
    print(f"{m} is not an anagram of {n}.")