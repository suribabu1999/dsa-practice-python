sorted_uniq_list = [1,2,3,4,5,6]

#first 1 
#second 1 + 2
#third 1 + 2 + 3
n = len(sorted_uniq_list)

#..so on

pre_list = [0] * (n+1)
print(pre_list)

for i in range(n):
    pre_list[i+1] = pre_list[i] + sorted_uniq_list[i]

print(pre_list)