List=eval(input("List: "))
print("Initial List:", List)   # printing the initial list
n = len(List)
k = 0

while k <= n:     # for repeating till all elements gets sorted
    for i in range(n-1):    # accessing each element of the list
        if List[i] > List[i+1]:  # swapping if current element > second
            List[i], List[i+1] = List[i+1], List[i]     # swapping logic
        else:       # if current element < continue
            continue
    k += 1
print(List)

'''
                              BUBBLE SORT
                            ---------------
The basic idea of bubble sort is to comapre two adjescent values and exchange them if
they are not in proper order.

Eg:
    List=[11,15,4,5,89,70]
    in the first step:
        l=[11,4,5,15,70,89]     here heaviest element took the last place
                        repeat this process till all elements gets their ordered place

'''

'''
                                Algorithm:
                              --------------

take a list
print the initial list
find the length of the list
access each element of the list
	check whether the current element is greater than the next element
		if yes then swap their valuse
	else
		continue
do this till the end of the list
the heaviest element will get the last place 
again repeat the process so that the second heaviest element gets the second last place
do the process a number of times until all the elements gets their respective places

'''
