import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    # Partition into 3 parts
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Only recurse on less and greater
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)
