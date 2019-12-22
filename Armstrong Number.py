'''Armstrong number: number whose sum of cube of digits is equal
to the number.
Eg: 153=(1^3)+(5^3)+(3^3)'''

#Date: September 21st, 2019

num=int(input("Number: "))
temp=num
sum=0
while temp>0:
    x=temp%10
    sum=sum+(x**3)
    temp=temp//10
if sum==num:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")
