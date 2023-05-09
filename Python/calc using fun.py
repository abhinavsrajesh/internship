s=0
while(s!=5):
    s=int(input("Enter your choice:\n1.Add\n2.Sub\n3.Div\n4.Mul\n5.Exit\n"))

def add(a,b):
    return a+b
if s==1:
    a=int(input())
    b=int(input())
    print(add(a,b))

def sub(c,d):
    return c-d
if s==2:
    c=int(input())
    d=int(input())
    print(sub(c,d))

def div(e,f):
    return e/f
if s==3:
    e=int(input())
    f=int(input())
    print(div(e,f))

def mul(g,h):
    return g*h
if s==4:
    g=int(input())
    h=int(input())
    print(mul(g,h))


