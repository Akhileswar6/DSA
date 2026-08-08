def calPoints(operations):
    stack = []

    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))

    res = 0
    for i in stack:
        res += i

    return res
    

print(calPoints(["5","2","C","D","+"]))