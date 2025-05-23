def pal(s):
    s=s.lower()
    if len(s)<=1:
        return true
    elif s[0]!=s[-1]:
        return false
    else:
     return pal[1:-1]
myinput=input("enter a string:")
if pal(myinput):
    print(f"'{myinput}' is a pallidrone:")
else:
    print(f"'{myinput}' is not a pallidrone:")
