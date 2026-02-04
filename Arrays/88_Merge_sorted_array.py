def mergeSortedArray(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= len(nums2):
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

print(mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3))


