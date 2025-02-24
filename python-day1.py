"""Write a program to check if a given number is positive,
negative, or zero.
"""
num=int(input("Enter a number"))
res="Positive Number"if num>0 else "Zero"if num==0 else "Negative Number"
print(res)


"""Determine if a number is odd or even.
"""
num=int(input("Enter a number"))
res="Even Number"if num%2==0 else "Odd Number"
print(res)


"""Check if a person is eligible to vote (age >= 18)."""
age=int(input("Enter age"))
res="Eligible to vote" if age>=18 else "Not eligible to vote"
print(res)


"""Write a program to find the greatest of two numbers.
"""
num1=float(input("enter first number"))
num2=float(input("enter second number"))
if num1>num2:
    print(num1," is greater")
else:
    print(num2," is greater")



"""Print "Pass" if a student scores more than 40 marks;
otherwise, print "Fail."
"""
marks=float(input("Enter Marks"))
res="Pass"if marks>40 else "Fail"
print(res)


"""Write a program to display the day of the week based on a
 number input (1 for Monday, 2 for Tuesday, etc.).
# """
num=int(input("Enter a number"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid")


""" Implement a simple calculator to perform addition,
subtraction, multiplication, and division.
"""
calculater=input("Enter mathematical operation")

if calculater=="addition":
    num=float(input("Enter number"))
    print(num+num)
elif calculater=="subtraction":
    num=float(input("Enter number"))
    print(num-num)
elif calculater=="multiplication":
    num=float(input("Enter number"))
    print(num*num)
elif calculater=="division":
    num=float(input("Enter number"))
    print(num/num)
else:
    print("Invalid Operation")


"""Write a program to display the name of a month based on
the month number (1 for January, 2 for February, etc.).
"""
num=int(input("Enter a number"))
if num==1:
    print("january")
elif num==2:
    print("Febraury")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
    print("Invalid")


"""Write a program to find the greatest of three numbers.
"""
a=float(input("Enter First Number"))
b=float(input("Enter Second Number"))
c=float(input("Enter Third Number"))
if a>b and a>c:
    print(a," is greater number")
elif b>c and b>a:
    print(b," is greater number")
else:
    print(c," is greater number")


"""Check if a year is a leap year.
"""
year=int(input("Enter year"))
if (year%4==0 and year%100!=0) or (year%400==0): # 1700,1800,1900,2100 are divisible 4 and 100 but not a leap year
    print("Leap year")
else:
    print("not a leap year")


""" Write a program to classify a character entered by the user
as a vowel, consonant, or neither.
"""
char=input("Enter character")
if char.isalpha():
    if char in('a','e','i','o','u','A','E','I','O','U'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Neither")


""" Calculate the grade of a student based on the marks they
score:
1. 90-100: Grade A
2. 80-89: Grade B
3. 70-79: Grade C
4. <70: Fail.
"""
score=float(input("Enter Score"))
if score>=90 and score <=100:
    print("Grade A")
elif score>=80 and score <=89:
    print("Grade B")
elif score>=70 and score <=79:
    print("Grade c")
elif score<70:
    print("Fail")
else:
    print("Invalid Score")

    
"""Write a program to check if three sides length form a valid
triangle.
"""
# sum of two sides of triangles should be greater than third side
a=input("Enter First Side")
b=input("Enter Second Side")
c=input("Enter Third Side")
if a+b>c and a+c>b and b+a>c:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
