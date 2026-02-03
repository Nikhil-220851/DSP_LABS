import datetime
now = datetime.datetime.now()
print("The current time is:", now.strftime('%H:%M:%S'))
print("The current date is:", now.strftime('%Y-%m-%d'))
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)
n=int(input("Enter a number: "))
value=n+(n*n)+(n*n*n)
print("The calculated value is:", value)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a==b==c):
    calc_value=a*3
    print("The calculated value is:", calc_value)
else:
    calc_value=a+b+c
    print("The calculated value is:", calc_value)
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=(x+y)*(x+y)
print("The calculated value is:", z)
amount=int(input("Enter the pricipal amount: "))
r=float(input("Enter the rate of interest: "))
time_period=int(input("Enter the time period in years: "))
future_value=float(amount*(1+(r/100))**time_period)
print("The future value is:", future_value)
data=input("Enter some number: ")
try:
    val=int(data)
    print("The entered data is parsed as integer:", val)
except ValueError:
    try:
        val=float(data)
        print("The entered data is parsed as float:", val)
    except ValueError:
        print("The entered data is treated as string:", data)
m=input("Enter a number: ")
p=int(m)
digit_sum=0
nsum=(p*(p+1))//2
print("The sum of first "+m+" natural numbers is:",nsum)
number=int(input("Enter a number: "))
while number>0:
    digit=number%10
    digit_sum=digit_sum+digit
    number=number//10
print("The sum of digits is:", digit_sum)
char=input("Enter a character: ")
print("The ASCII value of '"+char+"' is:", ord(char))
str=input("Enter a string: ")
try:
    val=int(str)
    print("The entered string is number:", val)
except ValueError:
    print("The entered string is not a number:", str)
for i in range(5):
    for j in range(3):
        print("*", end=" ")
    print()
q=2000
while q<=3200:
    if q%7==0 and q%5!=0:
        print(q,end=",")
    q=q+1
C=50
H=30
values=input("Enter comma separated numbers: ")
items=values.split(",")
for d in items:
    Q=int(d)
    result=round((2*C*Q/H)**0.5)
    print("The calculated value for input", Q, "is:", result)
e=65
for i in range(6):
    for j in range(5-i):
        print(chr(e), end=" ")
        e=e+1
    print()