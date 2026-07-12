'''
Time complexity: O(n)
Space complexity: O(1)
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1
