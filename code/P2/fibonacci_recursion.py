def fibonacci_recursion(n):
    """calculate Fibonacci sequence using recursion"""
    if n < 3:  # n == 1 | n == 2
        return 1
    else:
        return fibonacci_recursion(n - 1) + \
               fibonacci_recursion(n - 2)


if __name__ == '__main__':
    for i in range(21):
        print(i, fibonacci_recursion(i))
