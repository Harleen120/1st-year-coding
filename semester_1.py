#Factorial
'''num=int(input("enter number:"))
c=1
for i in range(1,num+1):
    c=c*i
print(f'factorial of {num} is {c}')'''

#perfect number
'''num=int(input("enter number:"))
c=0
for i in range(1,num):
    if num%i==0:
        c+=in
if num==c:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')'''
  

#check for even number
'''num=int(input("enter number:"))
if num%2==0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')'''

#radius
'''r=int(input('enter radius of circle'))
if r<50:
    print('area =', 3.14*r*r)
else:
    print('unable to draw circle on paper')'''
       

#simple caalculator
'''while True:
    num1=float(input('enter number:'))
    op=input('enter operator:')
    num2=float(input('enter number:'))
    if op=='+':
        print(num1+num2)
    if op=='-':
        print(num1-num2)
    if op=='*':
        print(num1*num2)
    if num2!=0:
        if op=='/':
            print(num1/num2)
        if op=='//':
            print(num1//num2)
        if op=='%':
            print(num1%num2)
    else:
        print('not defined')
    print()'''



#simple calculator
'''while True:
    try:
        num1=float(input('enter number:'))
        op=input('enter operator:')
        num2=float(input('enter number:'))
        if op=='+':
            print(num1+num2)
        elif op=='-':
            print(num1-num2)
        elif op=='*':
            print(num1*num2)
        elif op=='/':
            print(num1/num2)
        elif op=='//':
            print(num1//num2)
        elif op=='%':
            print(num1%num2)
        else:
            print('invalid operator!')
   
    except ZeroDivisionError:
        print('not defined')
    except ValueError:
        print('invalid input!')
    print()'''    


#improved
'''while True:
    try:
        num=input('enter number or \'q\' to quit ')
        if num.lower()=='q':
            print('exit')
            break
    
        num1=float(num)
        op=input('enter operator:')
        num2=float(input('enter number:'))
        if op=='+':
            print(num1+num2)
        elif op=='-':
            print(num1-num2)             #elif to make it more efficient and time saving
        elif op=='*':
            print(num1*num2)
        elif op=='/':
            print(num1/num2)
        elif op=='//':
            print(num1//num2)
        elif op=='%':
            print(num1%num2)
        else:
            print('invalid operator!')
   
    except ZeroDivisionError:
        print('not defined')
    except ValueError:
        print('invalid input!')
    print()'''


#fibonacii series
'''def series():
    a=0
    b=1
    print(a,b,end=' ')
    c=a+b
    for i in range(3,num+1):
        a=b
        b=c
        print(c,end=' ')
        c=a+b
num=int(input('how many terms of series do u want '))
series()'''

#match case
'''m=int(input('enter marks:'))
match m:
    case _ if 90<=m<=100:
        print('a')
    case _ if m>=80 and m<90:
        print('B')
    case _ if 70<=m<80:
        print('C')
    case _ if 60<=m<70:
          print('D')
    case _:
        print('F')'''

#Greatest Common Divisor
'''x=int(input('x:'))
y=int(input('y:'))
if x==0 or y==0:
      print('value should be non zero')
else:
    b=0
    if x>y:
        b=x
    else:
        b=y
    while b>0:
        if x%b==0 and y%b==0:
            print('gcd:',b)
            break
        b-=1'''

#factorial
'''def fact(n):
    c=1
    for i in range (1,n+1):
       c*=i
    print(f'factorial of {n} is {c}')

n=int(input("enter no whose factorial you want"))
fact(n)'''

#Armstrong Number
def armstrong(num):
    n=num
    st=str(num)
    l=len(st)
    s=0
    while n>0:
        a=n%10 #ones digit of num
        s+=a**l
        n//=10 #floor division to remove last digit

    if s==num:
        print('%d is armstrong number'%(num))
    else:
        print('%d is not armstrong number'%(num))

num=int(input())
armstrong(num)
        










    


