# Assignments

# 1) Whether a no. is positive or negative

num=int(input('Enter a no:'))

if num>=0:
    print('Positive number')
else:
    print('Negative number')
    
# 2) Whether a no. is even or odd.

num=int(input('Enter a no:'))

if num%2==0:
    print('Even number')
else:
    print('Odd number')
    
# 3) Whether a person is eligible to vote or not

Age=int(input('Enter your age:'))

if Age>=18:
    print('You are eligible for vote')
else:
    print('You are not eligible for vote')
    
# 4) program to check whether a no>100

num=int(input('Enter a number:'))

if num>100:
    print('Number is greater than 100')
else:
    print('Number is not greater than 100')
    
# 5) program for leap year

year=int(input('Enter year:'))

if num%2==0:
    print('Leap Year')
else:
    print('Normal Year')
    
# 6) program for comparison for 2 nos

num1= int(input('Enter first no:'))
num2= int(input('Enter second no:'))

if num1>num2:
    print(num1,'is greater')
else:
    print(num2,'is greater')
    
# 7) Check character vowel or consonant

char= input('Enter Character:')
vowel=('a','e','i','o','u')

if char.lower() in vowel:
    print('Vowel')
else:
    print('Consonant')
    
# 8) A no is divisible by 5 or not

num= int(input('Enter a no:'))

if num%5==0:
    print('Divisible')
else:
    print('Not divisible')
    
# 9) A student has passed or failed

marks= int(input('Enter your marks:'))

if marks>=40:
    print('Pass')
else:
    print('Fail')
    
# 10) A num is single digit num or not

num= int(input('Enter a no:'))

if num>=0 and num<=9:
    print('Single digit number')
else:
    print('Not a single digit number')
    
# 11) temperature is hot or cold

temp= int(input('Enter temperature:'))

if temp>30:
    print('Hot')
else:
    print('Cold')
    
# 12) program to check age

age= int(input('Enter your age:'))

if age<18:
    print('Child')
else:
    print('Adult')
    
# 13) to check no. zero or non zero

num= int(input('Enter no:'))

if num==0:
    print('Zero')
else:
    print('Non zero')
    
# 14) program to check char uppercase or lowercase

char=input('Enter character:')

if char.isupper():
    print('Uppercase')
elif char.islower():
    print('Lowercase')
else:
    print('Not a character')
    
# 15) program greatest of 3 nos

num1=100
num2=50
num3=150

if num1>=num2 and num1>=num3:
    print('Greatest number is:',num1)
elif num2>=num1 and num2>=num3:
    print('Greatest number is:',num2)
else:
    print('Greatest number is:',num3)
    
# 16) num is divisible by both 3&7 or not

num= int(input('Enter no:'))

if num%3==0 and num%7==0:
    print('Divisible by both 3 and 7')
else:
    print('Not divisible by both 3 and 7')
    
# 17) check grade based on marks(A,B,C,Fail)

marks= int(input('Enter marks:'))

if marks>=75:
    print('Grade:A')
elif marks<=75 and marks>=50:
    print('Grade:B')
elif marks<=50 and marks>=30:
    print('Grade:C')
else:
    print('Fail')
    
# 18) whether a no is positive,negative or zero

num=int(input('Enter no:'))

if num>0:
    print('Positive no')
elif num==0:
    print('Zero')
elif num<0:
    print('Negative no')
    
# 19) program to print day name based on day no(1-7)

day=int(input('Enter day no:'))

if day==1:
    print('Monday')
elif day==2:
    print('Tuesday')
elif day==3:
    print('Wednesday')
elif day==4:
    print('Thursday')
elif day==5:
    print('Friday')
elif day==6:
    print('Saturday')
elif day==7:
    print('Sunday')
    
# 20) program to check ticket price on age

age= int(input('Enter Age:'))

if age>=75:
    print('Ticket Price:₹250')
elif age<75 and age>=60:
    print('Ticket Price:₹500')
elif age<60 and age>=18:
    print('Ticket Price:₹1000')
elif age<18:
    print('Ticket Price:₹350')
    
# 21) smallest of 3 nos

a= int(input('Enter 1st no:'))
b= int(input('Enter 2nd no:'))
c= int(input('Enter 3rs no:'))

if a<b and a<c:
    print('a is smallest:',a)
elif b<a and b<c:
    print('b is smallest:',b)
else:
    print('c is smallest:',c)


# 22) salary bonus based on years of service

service= int(input('Enter your years of service:'))

if service>=5:
    print('Salary bonus(₹):2000')
elif service>=10:
    print('Salary bonus(₹):4000')
elif service>=20:
    print('Salary bonus(₹):6000')
elif service>=30:
    print('Salary bonus(₹):10000')
elif service>=35 and service<=40:
    print('Salary bonus(₹):13000')
    
# 23) calculate electricity bill based on units consumed

units_consumed= int(input('Enter units consumed:'))

if units_consumed<=100:
    Total_bill=4.75*units_consumed
elif units_consumed<=200:
    Total_bill=7.0*units_consumed
elif units_consumed<=300:
    Total_bill=10.5*units_consumed
elif units_consumed<=400:
    Total_bill=13.5*units_consumed
elif units_consumed<=500 and units_consumed>=500:
    Total_bill=16.5*units_consumed
    
print(Total_bill)
    
# 24) program to check exam results(Destinction,first class,pass,fail)

Total_obt_marks= int(input('Enter total obt marks:'))

if Total_obt_marks>=500:
    print('Distinction')
elif Total_obt_marks>=300 and Total_obt_marks<500:
    print('First class')
elif Total_obt_marks>=200 and Total_obt_marks<300:
    print('Pass')
elif Total_obt_marks<200:
    print('Fail')
    
# 25) triangle type checker

a= float(input('Enter side a:'))
b= float(input('Enter side b:'))
c= float(input('Enter side c:'))

if a==b==c:
    print('Equilateral')
elif a==b or b==c or a==c:
    print('Isoscales')
else:
    print('Scalene')
    
# 26) check month names based on month no.

month= int(input('Enter month no:'))

if month==1:
    print('January')
elif month==2:
    print('February')
elif month==3:
    print('March')
elif month==4:
    print('April')
elif month==5:
    print('May')
elif month==6:
    print('June')
elif month==7:
    print('July')
elif month==8:
    print('August')
elif month==9:
    print('September')
elif month==10:
    print('October')
elif month==11:
    print('November')
elif month==12:
    print('December')
else:
    print('Invalid number')
    
# 27) check login status based on username and password

username= input('Enter Username-->')
password= input('Enter password-->')

if username== 'Unix123' and password== 'Fu457Jo&uEXGhj':
    print('Login Successful')
else:
    print('Please check entered username or password')

# 28) calculate discount based on total shopping amount

total_amount= int(input('Enter total amount:'))

if total_amount>=2000 and total_amount<4000:
    discount=total_amount/100*10
    print('Discount',discount)
elif total_amount>=4000 and total_amount<10000:
    discount= total_amount/100*20
    print('Discount',discount)
elif total_amount>=10000:
    discount= total_amount/100*30
    print('Discount:',discount)

# 29) blood donation eligiblity based on age and weight

age = int(input('Enter your age:'))
weight= float(input('Enter your weight:'))

if age>=18 and weight>=45:
    print('Eligible for blood donation')
else:
    print('Not eligible for blood donation')
    
# 30) check the type of no(single,double,three digit)

num= int(input('Enter no:'))

if num>=0 and num<=9:
    print('Single digit number')
elif num>=10 and num<=99:
    print('Two digit number')
elif num>=100 and num<=999:
    print('Three digit number')
    
# 31) whether a no positive or negative

num= int(input('Enter number:'))

if num>=0:
    print('Positive')
    if num%2==0:
        print('Even')
    else:
        print('Odd')
else:
    print('Negative')
    
# 32) whether a student eligible for exam (attendance+marks)

attend= int(input('Enter Attendance(%):'))
marks= int(input('Enter marks(out of 50):'))

if attend>=75 and marks>=25:
    print('Eligible for exam')
else:
    print('Not eligible for exam')
    
# 33) check whether a person apply for loan

credit_score= int(input('Enter your credit score:'))
account_balance = int(input('Enter account balance:'))

if credit_score>=750 and account_balance>=25000:
    print('Your are eligible. please apply for loan!')
else:
    print('You are not eligible. please add fund to your account or increase credit score!')
    
# 34) whether a year is leap year and centuary year

year= int(input('Enter year:'))

if year%2==0:
    print('Leap year')
elif year%100==0:
    print('Centuary year')
    

# 35) whether a no divisible by 3 & 5

num= int(input('Enter a no:'))

if num%3==0 and num%5==0:
    print('Divisible by 3 & 5')
else:
    print('Not divisible 3 & 5')

# 36) whether a person is elgible for driving license

age=int(input('Enter your age:'))

if age>=18:
    print('Eligible for driving license')
else:
    print('Not eligible for driving license')
    
# 37) whether a no lies bet. 30 & 50

num= int(input('Enter a no:'))

if num>=10 and num<=50:
    print('No. lies bet. 10 & 50')
else:
    print('No. does not lies bet. 10 & 50')
    
# 38) whether a student passed all subjects
print('Out of marks:1000')
obt_marks= int(input('Enter total marks:'))

if obt_marks>=400:
    print('Student passed all subjects.')
else:
    print('Student not passed all subjects')
    
# 39) whether a no. greater than 0 and less than 100

num= int(input('Enter no:'))

if num>0 and num<100:
    print('Number is greater than 0 and less than 100')
else:
    print('Number is not greater than 0 and less than 100')
    
# 40) whether a password is valid or not (nested if)

password= input('Enter password-->')

if len(password)>=8:
    if '0'in password or '1'in password or '2'in password or '3'in password or '4'in password or '5'in password or '6'in password or '7'in password or '8'in password or '9'in password:
        print('Valid Password')
    else:
        print('Invalid Password')
    
else:
    print('Invalid Password')

# 41) program to print weekday name using math case

weekday= int(input('Enter weekday no:'))

match weekday:
    case 1:
     print('Monday')
    
    case 2:
     print('Tuesday')
    
    case 3:
     print('Wednesday')
    
    case 4:
     print('Thursday')
    
    case 5:
     print('Friday')
    
    case 6:
     print('Saturday')
    
    case 7:
     print('Sunday')
    
    
# 42) program to perform calculator operations using match case

num1= int(input('Enter 1st no:'))
num2= int(input('Enter 2nd no:'))
result=num1,num2
choice=input('Enter choice:')

match choice:
    case '+':
     print('Addition')
     result=num1+num2
    
    case '-':
     print('Subtraction')
     result=num1-num2
    
    case '*':
     print('Multiplication')
     result=num1*num2
    
    case '/':
     print('Division')
     result=num1/num2
    
    case '%':
     print('Modulus')
     result=num1%num2
    
    case '**':
     print('Power')
     result=num1**num2
    
# 43)print month days using match case

month=input('Enter month:')

match month:
    case 'January':
      print('Days:30')
      
    case 'February':
      print('Days:28/29')
      
    case 'March':
      print('Days:31')
      
    case 'April':
      print('Days:30')
      
    case 'May':
      print('Days:31')
      
    case 'June':
      print('Days:30')
      
    case 'July':
      print('Days:31')
      
    case 'August':
      print('Days:31')
      
    case 'September':
      print('Days:30')
      
    case 'October':
      print('Days:31')
      
    case 'November':
      print('Days:30')
      
    case 'December':
      print('Days:31')
      
# 44) check traffic signal actions using match case

choice=int(input('Enter your choice:'))

match choice:
    case 1:
      print('Red:Stop')
    case 2:
      print('Yellow:Go slow')
    case 3:
      print('Green:Go')
      
# 45) print menu based food selection using match case

choice= int(input('Enter no to chose food:'))

match choice:
    case 1:
      print('Gulab Jamun')
    case 2:
      print('Rabdi')
    case 3:
      print('Rasmalai')
    case 4:
      print('Jilebi')
    case 5:
      print('Samosa')
      
# 46) print grade discription using match case

choice= int(input('Enter choice'))

match choice:
    case 1:
      print('A+: if marks greater than equal to 75')
    case 2:
      print('A: if marks greater than equal to 60 and less than 75')
    case 3:
      print('B+: if marks greater than equal to 50 and less than 60')
    case 4:
      print('B: if marks greater than equal to 40 and less than 50')
    case 5:
      print('Pass: if marks greater than equal to 30 and less than 40')
    case 6:
      print('Fail: if marks greater than 0 and less than 30')
      
# 47) check user role[admin,user,guest] using match case

choice= int(input('Enter choice:'))

match choice:
    case 1:
      print('Admin')
    case 2:
      print('User')
    case 3:
      print('Guest')
      
# 48) program to print lang choice using match

choice=int(input('Enter choice:'))

match choice:
    case 1:
      print('Marathi')
    case 2:
      print('English')
    case 3:
      print('Konkani')
    case _:
      print('Invalid choice')

# 49) print result status using match

choice= int(input('Enter choice:'))

match choice:
    case 1:
      print('Pass')
    case 2:
      print('Fail')
      
# 50) build a simple ATM menu 

choice= int(input('Enter choice number:'))

print('1: check balance')
print('2: Deposit funds')
print('3: withdraw funds')
print('4: exit')
bal=10000
match choice:
    case 1:
      bal=10000
      print('Balance:',bal)
    case 2:
      Deposit=int(input('Enter amount:'))
      bal+=Deposit
    case 3:
      withdraw=int(input('Enter withdraw amount:'))
      bal-=withdraw
    case 4:
      print('Exit. thank you!')
    case _:
      print('Invalid choice')
    
    
print('===========The End===========')
# The End