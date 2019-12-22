#   insertion sort

List=eval(input("List: "))
print("Initial: ", List)    # print the initial list
length=len(List)

for i in range(length-1):       # accessing each element of the main list
    if List[i] > List[i+1]:     # comparing current element with the next element
        List[i], List[i+1] = List[i+1], List[i]     # swapping values

        for j in range(i-1, 0, -1):     # comparing values sorted earlier only when the current value is swapped
            if List[j] > List[j+1]:     # swapping he new value with the earlier value
                List[j], List[j+1] = List[j+1], List[j]

print(List)

'''
        Insertion Sort
    ---------------------
    
    in this, the program divides the list into two parts, a sorted and an unsorted part
    the sorted part contains the values which are already sorted and the unsorted one contains the opposite
    now it will compare the value next to the sorted part with the value of the last element of the sorted part
    then it places the new element in the sorted section in its right position
    
    Eg:
        List=[12,4,15,14,32]
        1st step: [4,12,15,14,32]
        2nd step: [4,12,14,15,32]
        3rd step: [4,12,14,15,32]
        4th step: [4,12,14,15,32]
        end of the process
        
'''

'''
                                algorithm:
                             ----------------

take a list
display initial list
get the length of the list
access each values of the list
	compare first(x) value with the second(y) value
	if x > y
		swap x with y
		now compare the values of y with the values before it
			again swap if y < previous number
	else
		continue


'''
