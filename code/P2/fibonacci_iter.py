# Calculate Fibonacci sequence using iteration

N = 20
fib = [1, 1]
for i in range(2, N):
    fib.append(fib[i-1] + fib[i-2])
    
print(fib)
