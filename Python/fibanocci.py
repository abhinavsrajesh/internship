a=0
b=1 
sum=0
c=int(input("Enter a limit:"))
print(a)
print(b)
while(sum<=c):
    sum=a+b
    if sum<=c:
        print(sum)
    else:
        break
    a=b
    b=sum
