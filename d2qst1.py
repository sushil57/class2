print("select the operation :\n", "1. ADD\n","2. sub\n", "3. multiply\n", "4. divide\n")
key = input("select the value 1,2,3,4\n")
num_1 = int(input("enter the first number :1"))
num_2 = int(input("enter the second number :"))
if key == "1":
    add = (num_1 + num_2)
    print (num_1 ,"+",num_2,"=", add)
elif key == "2":
    sub = (num_1 - num_2)
    print(num_1, "-", num_2, "=", sub)
elif key == "3":
    mul = (num_1 * num_2)
    print(num_1, "*", num_2, "=", mul)
elif key == "4":
    divide = (num_1 / num_2)
    print(num_1, "/", num_2, "=", divide)
else:
    print("invilid")


