'''
10.5 Sparse Search: 
Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.
EXAMPLE
Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4
'''

'''
- problem: dk to go left or right if the limits are "".
- do normal binary search.
    - at each point if "", just go left until found non-empty string.
        - if nothing, then go R
        - if found_string < target, go R
        - else: go L

'''
def sparseSearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # get mid to be a string by picking the closest left or right string that is non empty.
        if not arr[mid]:
            left, right = mid - 1, mid + 1
            while True:
                # out of bounds without finding anything, return false
                if left < low and right > high:
                    return -1
                if left >= low and arr[left]:
                    mid = left
                    break
                if right <= high and arr[right]:
                    mid = right
                    break
                left -= 1
                right += 1

        if not arr[mid] or arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
target = "ball"
assert sparseSearch(arr, target) == 4

arr = ["", "", "", "", "", "", "", "", "", "", "ball", "", ""]
target = "ball"
assert sparseSearch(arr, target) == 10

arr = ["ball", "", "", "", "", "", "", "", "", "", "ball", "", ""]
target = "ball"
assert sparseSearch(arr, target) == 0 or 10

arr = ["ball", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
target = "ball"
assert sparseSearch(arr, target) == 0

arr = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
target = "ball"
assert sparseSearch(arr, target) == -1
print("All test cases passed!")

        


