def reverseVowels(s):
    vowels = "aeiouAEIOU"
    left, right = 0, len(s) - 1
    chars = list(s)

    while left < right:

        while left < right and chars[left] not in vowels:
            left += 1
        
        while left < right and chars[right] not in vowels:
            right -= 1

        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)

print(reverseVowels("heLlo"))