def fibonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-2)+fibonacci(number-1)
number=int(input("enter the fibonacci number range:"))
sum=0
for num in range(number):
    print(fibonacci(num),end='')
    sum=sum+fibonacci(num)
    print("\n the sum of fibonacci series number:%d"%sum)
