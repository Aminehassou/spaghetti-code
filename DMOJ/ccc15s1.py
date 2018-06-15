add = 0
k = int(input())
nums = []
for x in range(k):
    nums.append(int(input()))
while 0 in nums:
    for index in range(len(nums)):
        if index > 0:
            if nums[index] == 0:
                del nums[index-1]
                del nums[index-1]
                break
for number in nums:
    add += number
print(add)