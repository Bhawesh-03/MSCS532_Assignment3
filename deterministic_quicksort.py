def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)
