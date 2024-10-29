import time
import random

# Sorting algorithm implementations

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def measure_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr.copy()) if sort_function == quick_sort else sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

array_size = 1000  

best_case_array = list(range(array_size))

average_case_array = best_case_array[:]
random.shuffle(average_case_array)

worst_case_array = list(range(array_size, 0, -1))
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": lambda arr: quick_sort(arr)
}
arrays = {
    "Best Case": best_case_array,
    "Average Case": average_case_array,
    "Worst Case": worst_case_array
}

results = {}
for sort_name, sort_function in sorting_algorithms.items():
    results[sort_name] = {}
    print(f"\nResults for {sort_name}:")
    for case_name, array in arrays.items():
        exec_time = measure_time(sort_function, array)
        results[sort_name][case_name] = exec_time
        print(f"{case_name}: {exec_time:.6f} seconds")
