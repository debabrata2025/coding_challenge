def longestSubarray(nums):
    zeroCount = 0
    maxlength = 0
    i = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            zeroCount += 1
        while zeroCount > 1:
            if nums[i] == 0:
                zeroCount -= 1
            i += 1
        maxlength = max(maxlength, j - i)

    return maxlength

num1 = [1,1,0,1]
num2 = [1,1,1]
num3 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(longestSubarray(num1))
print(longestSubarray(num2))
print(longestSubarray(num3))
