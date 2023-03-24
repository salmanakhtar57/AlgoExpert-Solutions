# Given: an array of integers and a target sum 
# Return: the indices of the two numbers that add up to the target sum
# Return empty array if no two numbers add up to the target sum
# You must add two different numbers in the array

def twoNumberSum(array, target_Sum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_Sum:
                return [array[i], array[j]]
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))            
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15))