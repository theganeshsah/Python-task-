#simple calculator with basic arithmetic operations of two number
x = float(input("enter first number : "))
op = input("enter mathematical operator : ")
y = float(input("enter second number : "))
if op=="+":
    print(x+y)
elif op=="-":
    print(x-y)
elif op=="*":
    print(x*y)
elif op=="/":
    print(x/y)