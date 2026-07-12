'''
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    smaller = []
    equal = []
    greater = []

    for element in arr:
        if element > pivot:
            greater.append(element)
        elif element == pivot:
            equal.append(element)
        elif element < pivot:
            smaller.append(element)

    sorted_list = []
    sorted_list.extend(quick_sort(smaller))
    sorted_list.extend(equal)
    sorted_list.extend(quick_sort(greater))

    return sorted_list
