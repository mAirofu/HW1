ex_bals = int(input("Enter your exam bals:"))
if ex_bals <= 49:
    print("Your rating is: Bad")
elif ex_bals <= 69:
    print("Your rating is: Okay")
elif ex_bals <= 89:
    print("Your rating is: Good")
elif ex_bals <= 100:
    print("Your rating is: Excelent")
else:
    print("Your rating is: Unknown")
