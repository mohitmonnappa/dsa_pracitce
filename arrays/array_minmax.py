"""
Given an array of size N. The task is to find the maximum and the minimum element of the array using the
minimum number of comparisons.
Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35
"""


def ret_min(arr):
    min, l = arr[0], len(arr)
    for i in range(1, l):
        if min > arr[i]:
            min = arr[i]
    print(f"Minimum element is {min}")


def ret_max(arr):
    max, l = arr[0], len(arr)
    for i in range(1, l):
        if max < arr[i]:
            max = arr[i]
    print(f"Maximum element is {max}")


test_cases = [[3, 5, 4, 1, 9], [22, 14, 8, 17, 35, 3]]

for i in test_cases:
    print(f"Input: arr[] = {i}")
    ret_min(i)
    ret_max(i)
