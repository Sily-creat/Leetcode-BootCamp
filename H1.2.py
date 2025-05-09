def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n  # Initialize the result array with 1s

    # Step 1: Compute the left product for each index
    left_product = 1
    for i in range(n):
        result[i] = left_product  # Store the left product in the result array
        left_product *= nums[i]  # Update the left product for the next index

    # Step 2: Compute the right product and multiply with the left product
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product  # Multiply with the right product
        right_product *= nums[i]  # Update the right product for the next index

    return result
