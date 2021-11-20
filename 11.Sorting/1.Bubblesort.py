def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums= [5,3,6,3,8,9,7,0,18,11]
sort(nums)
print(nums)

#problem swapping we use selection sort