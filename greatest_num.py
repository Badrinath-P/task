def next_greater_number(r, n):
    n = list(map(int, n))
    i = r - 2
    
    while i >= 0 and n[i] >= n[i+1]:
        i -= 1
    
    if i == -1:
        return "Not Possible"
    
    j = r - 1
    while n[j] <= n[i]:
        j -= 1
    
    n[i], n[j] = n[j], n[i]
    n[i+1:] = sorted(n[i+1:])
    
    return ''.join(map(str, n))

# Example usage
r = int(input())
n = input()
result = next_greater_number(r, n)
print(result)