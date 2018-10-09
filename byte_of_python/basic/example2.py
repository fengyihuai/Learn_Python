def twice(n):
    n *= 2
    return n

a = input("a:")
b = input("b:")
#print("====a,b:",a,b)
if a>3:
    b += 4
    #print("====1 b:",b)
    if b>5:
        c = a + twice(b)
        #print("====2 b:",b)
    if b<1:
        c = a - twice(b)
        #print("====3 c:",c)
    else:
        c = twice(a) - b
        #print("====4 c:",c)
print(c)
