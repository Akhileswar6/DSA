def maxAverageSubArray(nums,k):
    curr_sum = 0

    for i in range(k):
        curr_sum += nums[i]

    max_avg = curr_sum / k

    for i in range(k,len(nums)):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]

        avg = curr_sum / k
        max_avg = max(max_avg, avg)

    return max_avg

print(maxAverageSubArray([12,24,9,-5,3],4))
print(maxAverageSubArray([1,12,-5,-6,50,3],4))