year = int(input("please: "))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("ok")
elif year % 4 == 0 and year < 500:
    print("ok")
else:
    print("no")
