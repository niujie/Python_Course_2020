def is_prime_v1(n):
  """Return 'True' if 'n' is a prime number.
     False otherwise"""
  if n == 1:
    return False  # 1 is not prime
  for d in range(2, n):
    if n % d == 0:
      return False
  return True

# ===== Test Function =====
for n in range(1, 21):
  print(n, is_prime_v1(n))

import time

# ===== Time Function =====
t0 = time.time()
for n in range(1, 100000):
  is_prime_v1(n)

t1 = time.time()
print("Time required: ", t1 - t0)

import math
def is_prime_v2(n):
  """Return 'True' if 'n' is a prime number.
     False otherwise."""
  if n == 1:
    return False

  max_divisor = int(math.floor(math.sqrt(n)))
  for d in range(2, 1 + max_divisor):
    if n % d == 0:
      return False

  return True

# ===== Test Function =====
for n in range(1, 21):
  print(n, is_prime_v2(n))

# ===== Time Function =====
t0 = time.time()
for n in range(1, 100000):
  is_prime_v2(n)

t1 = time.time()
print("Time required: ", t1 - t0)

def is_prime_v3(n):
  """Return 'True' if 'n' is a prime number.
     False otherwise."""
  if n == 1:
    return False
  # if it's even and not 2, then it's not prime
  if n == 2:
    return True
  if n > 2 and n % 2 == 0:
    return False
  max_divisor = int(math.floor(math.sqrt(n)))
  for d in range(3, 1 + max_divisor, 2):
    if n % d == 0:
      return False
  return True

# ===== Test Function =====
for n in range(1, 21):
  print(n, is_prime_v3(n))

# ===== Time Function =====
# Write a script file and run in terminal
t0 = time.time()
for n in range(1, 100000):
  is_prime_v3(n)

t1 = time.time()
print("Time required: ", t1 - t0)  # much better
