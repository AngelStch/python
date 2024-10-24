def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of the Longest Increasing Subsequence is: {length_of_lis(nums)}")


import bisect

def length_of_lis_optimized(nums):
    if not nums:
        return 0

    lis = []  

    for num in nums:
        pos = bisect.bisect_left(lis, num)  
        if pos < len(lis):
            lis[pos] = num  
        else:
            lis.append(num)  

    return len(lis)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of the Longest Increasing Subsequence is: {length_of_lis_optimized(nums)}")
