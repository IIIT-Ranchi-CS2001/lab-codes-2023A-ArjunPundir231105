# squares of first n natural numbers

n = int(input("Enter the value of n: "))
i = 1
print("Number Square")

while (i <= n):
    print(f"{i}\t{i*i}")
    i += 1
    
# sum of the digits of the given number using a while loop


num = int(input("Enter a number: "))

sum = 0
i = num

while i > 0:
    digit = i % 10
    sum += digit
    i //= 10  


print(f"The sum of the digits of the number {num} is {sum}")
# Fibonacci series using while loop
n = int(input("Enter the number of terms: "))


a, b = 0, 1
i = 0

if n == 1:
    print(f"Fibonacci sequence up to {n}:")
    print(a)
else:
    print("Fibonacci sequence:")
    while i < n:
        print(a, end=" ")
        a, b = b, a + b
        i += 1