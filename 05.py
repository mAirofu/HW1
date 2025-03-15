y_num = int(input("Enter your number:"))
list_num = []
while y_num != 1:
    r_num = y_num % 2
    if r_num == 0:
        list_num.append(y_num)
    y_num -= 1
print(list_num)
