print("Enter two numbers")
a=int(input())
b=int(input())
c=int(input("Choose your operator:\n1.ADD\n2.SUBTRACT\n3.DIVIDE\n4.MULTIPLY\n"))
if c==1:
    print(a+b)
if c==2:
    print(a-b)
if c==3:
    print(a/b)
if c==4:
    print(a*b)
