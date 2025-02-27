# 1)Question 1
for i in range(1,101):
    print(i)
    
# 2)first n natural numbers
n=int(input())
res=((n*(n+1)/2))
print(res)

# 3)even numbers
n=int(input())
num=1
while(num<n+1):
    if num%2 == 0:
        print(num)
    num+=1

# 4)multiplication
n=int(input("enter the number"))
for i in range(1,21):
    print(n,"*",i,"=",n*i)

# 4.2)multiplication 1 to 8 table
n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print()


# 5 & 6)Reverse a num using while loop and count the n.o of digits
num=int(input())
n=num
rev_num=0
count=0
digit_sum=0
while num>0:
    rem=num%10
    count+=1
    digit_sum+=rem
    rev_num=rev_num*10 + rem
    num=num//10
print(rev_num)
print(digit_sum)
print(count)
if(rev_num==n):
    print("palindrome")
else:
    print("Not a palindrome")

# 7)stop entring negative n.o
while(1):
    n=int(input())
    if(n<0):
        break
    




#medium questions

#1)Fionacci
n=int(input())
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
    
# 2)prime number
n=int(input())
if(n==1):
    print("one is not prime and nor a composite")
elif(n<=0):
    print("enterd invalid number")
    
for i in range(2,n//2):
    if n%i == 0:
        print("not a prime number")
        break
    else:
        print("it is prime number")
        break


# 3)factorial using while loop
n=int(input("enter the number"))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i+=1
print(fact)

#question 4
n=int(input())
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i)

# question 5
while(1):
    print("\nmenu dirven program")
    print("1.find the square of a num")
    print("2.find the cube of a num")
    print("3.exit")
    
    n=input()
    if n=="square":
        x=int(input())
        print(x*x)
    elif n=="cube":
        x=int(input())
        print(x**3)
    elif n=="exit":
        print("exit the program")
        break
    else:
        print("invalid input")


#question 6
db_username="abhi"
db_password=123

n=int(input("enter the n.o of choices"))
while n>0:
    user_name=input("enter the user name")
    password=input("enter the passward")
    
    if user_name==db_username and password==db_password:
        print("login sucessfull")
        break
        #total chances can write zero also
    else:
        n-=1
        if(n==0):
            print("you have no chances")
            break
        print("invalid credentials")
        print("stil you have",n,"chances")        
