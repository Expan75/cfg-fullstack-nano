# Given an integer array containing duplicates, return the majority element if present.
# A majority element appears more than n/2 times, where n is the array size.
#
# E.g., the majority element 2 in the array: [2, 8, 7, 2, 5, 2, 3, 1, 2, 2]


numbers = [2,8,7,2,5,2,3,1,2,2]

# SOLUTION 1: Bruteforce O(n^2)
def find_majority_bf(numbers):
    for x in numbers:
        frequency = 0
        for y in numbers:
            if x == y:
                frequency += 1
        if frequency >= len(numbers)//2:
            return x
    return -1

# SOLUTION 2: Using a hashtable (dictionary), O(n) 
def find_majority(numbers):
    counts = {n: 1 for n in numbers}
    for number in numbers:
        counts[number] = counts[number]+1
        if counts[number] >= len(numbers)//2:
            return number
    return -1

#majority_number = find_majority(numbers)
majority_number = find_majority(numbers)
print(f"Majority is: {majority_number}")


# exam handout
# language req.
# no idea about extra time coding exercises?