"""
Given an array (or string), the task is to reverse the array/string.
Examples:

Input: original_array[] = {1, 2, 3} Output: array_reversed[] = {3, 2, 1}

Input: original_array[] = {4, 5, 1, 2} Output: array_reversed[] = {2, 1, 5, 4}
"""


# Not in place:
def extra_array_notinplace(arr):
    r = arr[::-1]
    print(f"Input: original_array[] = {arr} Output: array_reversed[] = {r}")


# in place, meaning using the same array and altering the positions in the array
def loop_inplace(arr):
    s, e = 0, len(arr) - 1
    print(f"Input: original_array[] = {arr}", end=" ")
    while s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    print(f"Output: array_reversed[] = {arr}")


# using recursion
def recursive(arr, s, e):
    if s >= e:
        return
    arr[s], arr[e] = arr[e], arr[s]
    recursive(arr, s + 1, e - 1)


test_cases = [[1, 2, 3], [4, 5, 1, 2]]
for i in test_cases:
    extra_array_notinplace(i)

for i in test_cases:
    loop_inplace(i)

for i in test_cases:
    print(f"Input: original_array[] = {i}", end=" ")
    recursive(i, 0, len(i) - 1)
    print(f"Output: array_reversed[] = {i}")