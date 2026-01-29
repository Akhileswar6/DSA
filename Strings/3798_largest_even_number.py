def largestEven(s):
    for i in range(len(s) -1, -1, -1):
        if s[i] == "2":
            return s[:i + 1]
    return ""

print(largestEven("1221"))