'''
Time complexity : O(logn)
Space complexity: O(1) 
'''

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while True:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1

    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 8))
