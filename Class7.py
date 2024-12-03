import random

N = int(input("Enter the upper limit (N) for random numbers: "))
K = int(input("Enter the number of random numbers to generate (K): "))

# Ensure K is at least 10
if K < 10:
    print("K should be at least 10. Setting K to 10.")
    K = 10

random_numbers = [random.randint(0, N) for _ in range(K)]
print("Generated list of random numbers:", random_numbers)