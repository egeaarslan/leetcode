def calculate(self, s: str) -> int:
    stack = []
    num = 0
    sign = 1  # 1 means positive, -1 means negative
    result = 0
    
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '+':
            result += sign * num
            num = 0
            sign = 1
        elif c == '-':
            result += sign * num
            num = 0
            sign = -1
        elif c == '(':
            # Push the current result and sign onto the stack, for later
            stack.append(result)
            stack.append(sign)
            # Reset the current result and sign
            result = 0
            sign = 1
        elif c == ')':
            # Complete the current number
            result += sign * num
            num = 0
            # Apply the sign before the parenthesis
            result *= stack.pop()  # stack.pop() is the sign before the parenthesis
            # Add to the result before the parenthesis
            result += stack.pop()
    
    result += sign * num  # Add the last number to the result
    return result