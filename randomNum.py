import random
import sys

num = int(input("How many random numbers do you want to generate"))
for i in range(num):
    print(random.randint(0, 100), end=",")
sys.exit()

