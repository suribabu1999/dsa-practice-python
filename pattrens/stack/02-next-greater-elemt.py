def nextGreater(nums):

    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)-1, -1, -1):

        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


print(nextGreater([2,1,3,5,4]))