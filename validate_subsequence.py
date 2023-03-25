#Given: Two non empty arrays.
# Find whether the second array is the subsequence of the first


def isValidSubsequence(array, sequence):
    sequence_index = 0
    for num in array:
        if num == sequence[sequence_index]:
            sequence_index += 1
        if sequence_index == len(sequence):
            return True
    return False

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [32, 2, 5]))

#Output:
#True
#False