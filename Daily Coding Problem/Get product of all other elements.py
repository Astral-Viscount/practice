"""
Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one
at i.
For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120,
60, 40, 30, 24]. Ifourinputwas [3, 2, 1],theexpectedoutputwouldbe [2,
3, 6]. 
"""

import math

arr = list(map(int, input().split()))

output =  []

for i, j in enumerate(arr):
    new = arr
    new.remove(j)
    res = math.prod(new)
    output.append(res)
    arr.insert(i, j)

print(output)
