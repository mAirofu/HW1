from_wich = int(input("From wich number:"))
to_wich = int(input("To wich number:"))
nums = from_wich
all_nums = []

if nums >= to_wich:
    print("Oops.. something went wrong, please restart code!")

cor_num = to_wich + 1

while nums != cor_num:
    all_nums.append(nums)
    nums += 1
print(all_nums)
