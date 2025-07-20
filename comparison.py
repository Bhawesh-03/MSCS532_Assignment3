import time
import random
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

def test_sorting_algorithms():
    sizes = [1000, 2000, 5000]
    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        arr_sorted = sorted(arr)
        arr_reversed = arr_sorted[::-1]
        arr_duplicates = [random.choice([1, 2, 3, 4]) for _ in range(size)]

        for name, func in [("Randomized", randomized_quicksort), ("Deterministic", deterministic_quicksort)]:
            for test_case, name_case in [(arr, "Random"), (arr_sorted, "Sorted"), (arr_reversed, "Reverse"), (arr_duplicates, "Duplicates")]:
                start = time.time()
                func(test_case.copy())
                end = time.time()
                print(f"{name} Quicksort on {name_case} array (size={size}): {end - start:.5f} sec")

test_sorting_algorithms()
