year = int(input("enter any year\n"))
if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")