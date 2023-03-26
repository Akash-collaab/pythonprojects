x = int(input("Enter a decimal number :"))
z=x
a =[]
while x>0:
    d = x%2
    a.append(d)
    n = n//2
a.reverse()
print("BInary equivalent of {0} is {1}".format(z,a))


