def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
x=input("enter the first interger:")
y=input("enter the second interger:")
if x.isdigit()and yisdigit():
    a=int(x)
    b=int(y)
    result=gcd(a,b)
    print(f"the gcd of{a}and{b} is:",result)
else:
    print("please enter vaild interger:")
