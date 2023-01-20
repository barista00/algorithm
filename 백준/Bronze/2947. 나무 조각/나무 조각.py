nums = list(map(int,input().split()))

while True:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            for j in nums:
                print(str(j),end=" ")
            print('')
    if [1,2,3,4,5] == nums:
        break