def backSpaceCompare(s, t):
    def build(string):
        stack = []
        for ch in string:
            if ch != "#":
                stack.append(ch)
            else:
                stack.pop()

        return "".join(stack)

    return build(s) == build(t)
    

print(backSpaceCompare('ab#c', "ad#c"))