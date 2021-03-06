#!/usr/bin/python3

# Array containing boxes' sizes. Boxes should be arranged sorted in non-decreasing order.
# Given an array, find the size of the minimum sequence that should be removed
# so the remaining boxes are in such an order
# Example: [1, 2, 3, 1, 1, 5]
# Either we remove (2, 3) or (1, 1). In any case, the elements to be removed are two

def solution(A):
    if A == []:
        return 0

    # Two pointers method

    # Traverse the array from right to left to find the first element who breaks the sorting
    # That will be the right pointer
    end = len(A) - 1
    current = A[len(A) - 1]
    while end - 1 >= 0 and current >= A[end]:
        current = A[end]
        end -= 1
    if current < A[end]:
        end += 1
    if end == 0:
        return 0

    # Traverse from left to right and, for every position in the array,
    # (that will be the left pointer)
    # count how many elements would maintain the order if we removed all in between both pointers
    # Move the right pointer if needed
    begin = 0
    previous = -1
    maximum = boxes = len(A) - end
    while A[begin] >= previous:
        if end >= len(A) or A[begin] <= A[end]:
            previous = A[begin]
            begin += 1
            boxes += 1
        else:
            end += 1
            boxes -= 1
        maximum = max(maximum, boxes)
    return len(A) - maximum
