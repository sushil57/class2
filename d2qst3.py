name = input("Enter your name\n")
age = int(input("Enter your age\n"))
mob = (input("Enter your mobile no\n"))
if name.isalpha() and age >= 18 and len(mob) == 10 and mob.isdigit():
    print("eligible for citizenship")
else:
    print(" not eligible for citizenship")