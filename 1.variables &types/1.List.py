#list
#list is mutable means we can change value
nums=[25,21,32,312,211,32]
nums
[25, 21, 32, 312, 211, 32]
nums[4]
211
nums[2:]
[32, 312, 211, 32]
nums[-1]
32
nums[-5]
21
nums[0]
25
nums[-1]
32
nums[-5]
21

names=['babab','asasa','ssa']
#correct
mil=[nums,names]
#correct
values=[9.5,'navin flour', 25] 

nums.append(45)
nums
[25, 21, 32, 312, 211, 32, 45]
nums.insert(2,77)
nums
[25, 21, 77, 32, 312, 211, 32, 45]

nums.remove(21)
nums
[25, 77, 32, 312, 211, 32, 45]
nums.pop()
45
nums
[25, 77, 32, 312, 211, 32]
del nums[2:]
nums
[25, 77]
nums.extend
sum(nums)
102
max(nums)
77
nums.sort()
nums
[25, 77]