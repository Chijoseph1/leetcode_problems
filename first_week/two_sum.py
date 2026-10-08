def two_sums1(nums,target):
    result = {}
    for index,value in enumerate(nums):
        # how to add ,how dictionary works 
        calculate = target - value
        # print(calculate)
        if calculate in result:
            return [result[calculate],index]
            
        else:
            result[value] = index

num = [2,4,8,7]
target = 9
print(two_sums1(num,target))

def target(nums,target):
    dic ={}
    for index in range(len(nums)):
        if target - nums[index] in dic:
            print(dic[target-nums[index]],index)
            break
        dic[nums[index]] = index
    else:
        print("no sum found")

nums = [1,2,3,4]
tar = 4
target(nums,tar)

def two_sums2(nums,target):
    result = {}
    for index,value in enumerate(nums):
        # how to add ,how dictionary works 
        calculate = target - value
        # print(calculate)
        if calculate in result:
            return [result[calculate],index]
        result[value] = index
    else:
        return "No sum found"

num = [2,2]
target = 9
print(two_sums2(num,target))