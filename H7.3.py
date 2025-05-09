def maxSubArray(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # Either start a new subarray or add to the current one
        max_sum = max(max_sum, current_sum)  # Update global max sum if necessary

    return max_sum
