def validAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


print(validAnagram("anagram", "najaram"))


# Brute Force
# def validAnagram(s, t):
#     if len(s) != len(t):
#         return False

#     t = list(t)

#     for num in s:
#         found = False

#         for i in range(len(t)):
#             if num == t[i]:
#                 t.pop(i)
#                 found = True
#                 break

#         if not found:
#             return False

#     return True

# print(validAnagram("anagram", "nagaram"))