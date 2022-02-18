nums = list(input().split( ))
first_num = list(nums[0])
second_num = list(nums[1])

first_num_s = 100*int(first_num[2])+10*int(first_num[1])+int(first_num[0])
second_num_s = 100*int(second_num[2])+10*int(second_num[1])+int(second_num[0])

if first_num_s > second_num_s:
    print(first_num_s)
else:
    print(second_num_s)