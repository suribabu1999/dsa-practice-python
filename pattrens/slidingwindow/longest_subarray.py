def longest_sub_array(arr, k):
    left = 0
    curr_sum = 0
    max_length = 0

    for right in range(len(arr)):
        curr_sum += arr[right]   # expand window
        print(f"Add {arr[right]}, Current sum = {curr_sum}")

        # shrink from left if sum > k
        while curr_sum > k and left <= right:
            print(f"Sum {curr_sum} > {k}, remove {arr[left]}")
            curr_sum -= arr[left]
            left += 1

        # update max_length
        max_length = max(max_length, right - left + 1)
        print(f"Window [{left}, {right}] length = {right-left+1}, Max = {max_length}")

    return max_length


print("Result =", longest_sub_array([1,2,3,4,5,6], 6))
