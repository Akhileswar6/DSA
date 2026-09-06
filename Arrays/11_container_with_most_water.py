def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        curr_height = min(height[left], height[right])
        curr_area = width * curr_height

        max_area = max(max_area, curr_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
    

print(maxArea([1,8,6,2,5,4,8,3,7]))



# Brute Force
# def maxArea(height):
#     max_area = 0

#     for i in range(len(height)):
#         for j in range(i+1, len(height)):
#             width = j-i
#             curr_height = min(height[i], height[j])
#             curr_area = width * curr_height

#             max_area = max(curr_area, max_area)

#     return max_area

# print(maxArea([1,8,6,2,5,4,8,3,7]))