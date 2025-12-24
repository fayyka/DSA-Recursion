def sum_numbers(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    return n + sum_numbers(n - 1)

# Example usage
print(sum_numbers(5)) 
