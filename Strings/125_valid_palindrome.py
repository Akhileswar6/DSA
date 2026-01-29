def isPalindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))