"""
Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have
a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

Examples:
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3
Output: Minimum Difference is 2

Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students
If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5
Output: Minimum Difference is 6

Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50} , m = 7
Output: Minimum Difference is 10
"""
# sliding window problem
# first sort the array
# we should compare the min and max element of each sub array(which is the window) and size is m
# initialize difference b/w first and last element of array to min1 and keep updating it if any difference
# is less than min1's value


def chocolate(case):
    t, m = case
    t = sorted(t)
    min1 = t[-1] - t[0]
    for j in range(m - 1, len(t)):
        min1 = min(min1, t[j] - t[j - m + 1])
    return f"Minimum difference is {min1}"


test_cases = [([7, 3, 2, 4, 9, 12, 56], 3), ([3, 4, 1, 9, 56, 7, 9, 12], 5), ([12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50], 7)]
for i in test_cases:
    print(f"Input: arr[] = {i[0]}")
    print(f"Output: {chocolate(i)}")
