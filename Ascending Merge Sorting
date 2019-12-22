"""merg sorting
when both the list entered are sorted
asc + asc = asc"""

list1 = eval(input("List1: "))
list2 = eval(input("List2: "))
list3 = list2+list1
print(list1)
print(list2)
l1 = len(list1)
l2 = len(list2)
chList1, chList2, chList3 = 0, 0, 0 
while chList1 <= l1-1 and chList2 <= l2-1:
	if list1[chList1] <= list2[chList2]:
		list3[chList3] = list1[chList1]
		chList3 += 1
		chList1 += 1
	else:
		list3[chList3] = list2[chList2]
		chList2 += 1
		chList3 += 1
if chList1 > l1-1:
	list3[chList3] = list2[chList2]
	chList2 += 1
	chList3 += 1
elif chList2 > l2-1:
	list3[chList3] = list1[chList1]
	chList3 += 1
	chList1 += 1
print(list3)
