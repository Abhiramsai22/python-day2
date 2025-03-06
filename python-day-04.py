
# sum of non prime digits
def check_prime(input_num):
    if input_num <= 1:
        return False
    for i in range(2, int(input_num**0.5) + 1):  # Optimized loop range
        if input_num % i == 0:
            return False
    return True
        
num = int(input("Enter the number: "))
sum_non_prime = 0

while num > 0:
    digit = num % 10  # Extract last digit
    if check_prime(digit)==False:  # Check if digit is not prime
        sum_non_prime += digit
    num //= 10  # Remove last digit

print("Sum of non-prime digits:", sum_non_prime)

# amstrong number

n=int(input("enter the number"))
temp=n
digits=len(str(n))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**digits
    #sum=sum+math.pow(rem,digits)
    n=n//10
if(temp==sum):
    print("amstrong number")
else:
    print("not a amstrong number")


# **********Task**********************


# 1)smallest prime digit in a number

n=int(input("enter the number"))
l=[]
while(n>0):
    temp=n%10
    if check_prime(temp)==True:
        l.append(temp)
    n=n//10
if len(l):
    print("the smallest prime in a given number",min(l))
else:
    print("No prime digits are there")
    
def check_prime(input_num):
    if input_num <= 1:
        return False
    for i in range(2, int(input_num**0.5) + 1):
        if input_num % i == 0:
            return False
    return True


# 2) sum of odd digits in a given number
n = int(input("Enter the number: "))
str1 = str(n)
sum= 0

for digit in str1:
    if int(digit) % 2 != 0:
        sum += int(digit)

print("Sum of odd digits:", sum)


# 3) Print all the Armstrong numbers in a given range

startrange=int(input("enter the min range for amstrong numbers"))
lastrange=int(input("enter the max range for amstrong numbers "))
for num in range(startrange,lastrange+1):
    temp=num
    digits=len(str(temp))
    sum=0
    while(temp>0):
        rem=temp%10
        sum=sum+rem**digits
        #sum=sum+math.pow(rem,digits)
        temp=temp//10
    if(num==sum):
        print(num)



# Nearest prime

# num=int(input("enter the number"))
# temp1=num

# right_side_prime=0
# while True:
#     temp1=temp1+1
#     if check_prime(temp1)==True:
#         right_side_prime=temp1
#         break
# print(right_side_prime)

# temp2=num
# left_side_prime=0
# while True:
#     temp2=temp2-1
#     if temp2<2:
#         break
#     if check_prime(temp2)==True:
#         left_side_prime=temp2
#         break
# print(left_side_prime)


# def check_prime(input_num):
#     if input_num <= 1:
#         return False
#     for i in range(2, int(input_num**0.5) + 1):  # Optimized loop range
#         if input_num % i == 0:
#             return False
#     return True

