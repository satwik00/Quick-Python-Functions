#for finding the multiples of  a single integer

#Date: April 5th, 2019

def multiples():
    nums=[] #empty array for storing divisible numbers
    x=int(input("Multiple of: "))   #number whose multiple is to be found
    n=int(input("Starting Number: "))   #strating from number
    m=int(input("Till Number: "))   #ending till number
    #loop for finding multiples
    while(n<=m ):
        if n%x==0:  #conditon if satisfied ammends the value in nums[]
            nums.append(n)
        n +=1   #incereasing the value by units
    print("Numbers are: ", nums)    #printing the numbers
