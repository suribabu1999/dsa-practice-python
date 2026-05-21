nums = (1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5)

freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(f"very frequest didgit in the tuple is  -------> {max(freq.values())} ")