# 21 and 6 appear twice → same frequency → not unique
# 89 appears once → only one with frequency 1 → unique

def firstUniquefreq(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    freq_count = {}
    for f in freq.values():
        freq_count[f] = freq_count.get(f, 0) + 1

    for num in nums:
        if freq_count[freq[num]] == 1:
            return num
        
    return -1

print(firstUniquefreq([21,89,12,21,6,6,2,2,2]))



