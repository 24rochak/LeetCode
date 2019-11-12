def evalRPN(tokens) -> int:
    stack = []
    for item in tokens:
        try:
            stack.append(int(item))
        except:
            a = stack.pop(-1)
            b = stack.pop(-1)
            if item == '*':
                stack.append(int(b) * int(a))
            elif item == '/':
                stack.append(int(int(b) / int(a)))
            elif item == '+':
                stack.append(int(b) + int(a))
            elif item == '-':
                stack.append(int(b) - int(a))

    return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
