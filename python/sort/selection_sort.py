'''

'''

def selection_sort(arr):
    current_sort = 0

    while current_sort <= len(arr)-2:
        smallest_number = arr[current_sort]
        smallest_index = current_sort

        for i in range(current_sort, len(arr)):
            if arr[i] < smallest_number:
                smallest_number = arr[i]
                smallest_index = i 

        if smallest_number != arr[current_sort]:
            temp = arr[current_sort]
            arr[current_sort] = smallest_number
            arr[smallest_index] = temp
        
        current_sort += 1

    return arr
