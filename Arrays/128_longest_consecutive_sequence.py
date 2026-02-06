def longestConsecutiveSequence(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in nums_set:
            length = 1
            current = num

            while current + 1 in nums_set:
                current += 1
                length += 1

            longest = max(longest, length)
            
    return longest

print(longestConsecutiveSequence([100,4,200,3,1,2]))