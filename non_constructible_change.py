#We have an array of positive non-zero integers.
#Each represents a coin but the value is not necessarily unique.
#We look at all the coins and return the minimum amount of change we cannot create.
#Mean we can give back change if possible from the given coins.
#We can use as many coins as we want.

def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1

print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
print(nonConstructibleChange([1, 1, 1, 1, 1]))

# Output:
# 20
# 6