def print_numbers(n):
    # Base case
    if n == 0:
        return
    # Recursive call
    print_numbers(n - 1)
    # Print after recursion to ensure ascending order
    print(n)

# Example usage
print_numbers(5)
