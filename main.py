def factorial_recursive(n):
    """
    Calculates the factorial of a non-negative integer using recursion.
    This function calls itself to solve smaller sub-problems.
    """
    # Base case: The condition that stops the recursion.
    # Factorial of 0 or 1 is 1.
    if n == 0 or n == 1:
        return 1
    # Recursive step: The function calls itself with a modified input (n-1).
    # n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Calculates the factorial of a non-negative integer using iteration (a loop).
    This provides a comparison to the recursive approach.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    test_number = 5

    print(f"--- Demonstrating Factorial Calculation for {test_number} ---")

    # Using the recursive function
    recursive_result = factorial_recursive(test_number)
    print(f"Recursive Factorial({test_number}): {recursive_result}")

    # Using the iterative function
    iterative_result = factorial_iterative(test_number)
    print(f"Iterative Factorial({test_number}): {iterative_result}")

    print("\n--- Testing Edge Cases ---")

    # Test with 0 (base case)
    print(f"Recursive Factorial(0): {factorial_recursive(0)}")
    print(f"Iterative Factorial(0): {factorial_iterative(0)}")

    # Test with 1 (base case)
    print(f"Recursive Factorial(1): {factorial_recursive(1)}")
    print(f"Iterative Factorial(1): {factorial_iterative(1)}")

    # Note on recursion limits: Python has a default recursion depth limit (e.g., 1000).
    # For very large numbers, iterative solutions are generally preferred to avoid
    # 'RecursionError: maximum recursion depth exceeded'.
