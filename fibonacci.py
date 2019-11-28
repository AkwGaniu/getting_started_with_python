# Fibonacci series

a, b = 0, 1
while a < 20:
    print(a, end=" ")
    a, b = b, a + b
    if a > 20:
        print(".")
