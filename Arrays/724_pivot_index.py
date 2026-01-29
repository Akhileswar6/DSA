def lengthOfLongestSubstringKDistinct(s,k):
    if k == 0:
        return 0
    
    freq = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

print(lengthOfLongestSubstringKDistinct("akhilaaa",2))

