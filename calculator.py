import math
print("\t___CALCULATOR__")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("\n The quotient is: %s"%q)
    print("\n The quotient is: %s"%r)
def square(a):
    x=math.sqrt(a)
    return x
while(True):
    print("\n\n Choose the operation you want to perform:")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE ROOT")
    print("\n\t6.EXIT")
    choice =int(input('>'))
    if choice==1:
        print("\n\nEnter the two number:")
        num1=int(input('>'))
        num2=int(input('>'))
        s=sum(num1,num2)
        print("The sum is:%s"%s)
    elif choice==2:
        print("\n\nEnter the two number:")
        num1=int(input('>'))
        num2=int(input('>'))
        p=sub(num1,num2)
        print("The sum is:%s"%p)
    elif choice==3:
       print("\n\nEnter the two number:")
       num1=int(input('>'))
       num2=int(input('>'))
       r=mul(num1,num2)
       print("The mul is:%s"%r)   
    elif choice==4:
        print("\n\nEnter the two number:")
        num1=int(input('>'))
        num2=int(input('>'))
        t=div(num1,num2)
        print("The Dvision is:%s"%t) 
    elif choice==5:
        print("\n\nEnter the only number:")
        num1=int(input('>'))
        t1=square(num1)
        print("The squre root  is:%s"%t1)
    else:
        print("you can exit Bye:")
        break
    
    
      