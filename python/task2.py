def missing_number(nums):
    n = len(nums)+1 
    for i in range(1, n + 1):
        if i not in nums:
            return(i)

result = missing_number([1, 2, 4, 5])
print(result) 
