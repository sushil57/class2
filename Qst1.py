#five marks as input
a = int(input("Enter first sub mark \n"))
b = int(input("Enter second sub mark \n"))
c = int(input("Enter third sub mark \n"))
d = int(input("Enter fourth sub mark \n"))
e = int(input("Enter fifth sub mark \n"))
l = []
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
add = sum(l)
print ("the sum of five sub mark is : ", add)