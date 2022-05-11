"""
We are going to solve one problem in 3 different ways to see how Time-Space complexity is affected.

TASK: Find first duplicate value
--------------------------------

Given an array of int between 1 and n, where n is the length of array, write a function that returns
the first int that appears more than once (when we read array left to right)
If no integer appears more than once, then we return -1.

Example 1
---------
input = [2,1,5,2,3,3,4]
output = 2

2 is the first integer that appears more than once. 3 also appears more than once, but
second 3 appears after second 2.


Example 2
---------
input = [2,1,5,3,3,2,4]
output = 3

3 is the first integer that appears more than once. 2 also appears more than once, but
second 2 appears after second 3.

return -1
"""
input = [2,1,5,2,3,3,4]
# input = [2,1,5,3,3,2,4]

# O(space=n)
def solution(input=input):
    seen = []
    for n_current in input:
        for n_seen in seen:
            if n_seen == n_current:
                return n_seen
        else: 
            seen.append(n_current)
    return -1


def solution1(input=input):
    seen = set()
    for n_current in input:
        if n_current in seen:
            return n_current
        else:
            seen.add(n_current)
    return -1


if __name__ == '__main__':
    print(solution())
    print(solution1())