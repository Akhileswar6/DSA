def intersection(nums1, nums2):
    values = set(nums1)
    res = set()

    for num in nums2:
        if num in values:
            res.add(num)
            
    return list(res)

print(intersection([4,9,5], [4,9,4,8,9]))
