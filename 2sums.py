def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  
            if nums[i] + nums[j] == target:
                return [i, j]  
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sums(nums, target)) 

def Optimized_sums(nums, target):
    num_dict = {}
    for i, num in enumerate(nums): # iterate over a list assigning index and value
        match = target - num 
        if match in num_dict: # checks if there is a matc hin num_dict
            return [num_dict[match], i] #returns the value and index 
        num_dict[num] = i # if not found store the number at the index
    return []


nums = [2, 7, 11, 15]
target = 9
print(two_sums(nums, target)) 

