'''Palamdrome Number: number whose digits on reversing forms
the same number.
Eg: 121=121'''

#Date: September 21st,2019

num=int(input("Number: "))
temp=num
sum=0
while temp>0:
    sum=sum*10 + (temp%10)
    temp=temp//10
if sum==num:
    print(num, "is a Palamdrome Number.")
else:
    print(num, "is not a Palamdrome Number.")
