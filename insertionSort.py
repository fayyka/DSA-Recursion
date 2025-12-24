def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]          # Current element to insert
        j = i - 1             # Index of the previous element

        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key

    return arr

# Example usage
numbers = [5, 3, 4, 1]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)
