y_num = int(input("Enter your number:"))
nums = 1
fact = 1
r_num = y_num + 1

while nums != r_num:
    fact = fact * nums
    nums += 1
print("Factorial of that number is:", fact)
