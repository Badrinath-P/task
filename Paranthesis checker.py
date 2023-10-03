def is_valid_expression(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Unmatched closing bracket
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False  # Mismatched closing bracket

    return len(stack) == 0  # Check if all brackets are matched


# Example usage
expression1 = "((()))"
expression2 = "((())"
expression3 = "()[]{}"
expression4 = "([)]"
expression5 = "{[()]}"
expression6 = "((()){}[])"

print(is_valid_expression(expression1))  # Output: True
print(is_valid_expression(expression2))  # Output: False
print(is_valid_expression(expression3))  # Output: True
print(is_valid_expression(expression4))  # Output: False
print(is_valid_expression(expression5))  # Output: True
print(is_valid_expression(expression6))  # Output: True
