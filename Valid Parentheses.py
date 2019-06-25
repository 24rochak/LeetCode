def isValid(s: str) -> bool:
    stack = []
    inv = {'[': ']', '(': ')', '{': '}'}
    for item in s:
        if item == '(' or item == '{' or item == '[':
            stack.append(item)
        elif len(stack) != 0:
            if inv[stack.pop()] != item:
                return False
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid("[][][]"))
