a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a,"is big")
    else:
        print(c, "is big")
elif b>c:
    print(b, "is big")
else:
    print(c, "is big")
