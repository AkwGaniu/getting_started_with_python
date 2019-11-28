def raise_to_power(num, power):
    result = 1
    for i in range(power):
        result = result * num
    return result


print(raise_to_power(5, 2))

# iterating through a list of string
string = "SHITO YOUTH FORUM"
print("**********Start*************")
for char in string:
    print("********** " + char + " **********")

print("***********End************\n\n")

# NESTED FOR LOOP
num_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print("***********************")
for i in range(len(num_array)):
    for j in range(len(num_array[i])):
        print("********** " + str(num_array[i][j]) + " **********")

print("***********************")
