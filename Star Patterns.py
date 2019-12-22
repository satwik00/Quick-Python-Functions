#Patterns

#Date: September 21st, 2019

'''Pattern 1:
*
**
***
........
'''

def p1():
    n=int(input("Columns: "))
    for a in range(1,n+1):
        print('*'*a)

'''Pattern 2:
.....
***
**
*
'''

def p2():
    n=int(input("Columns: "))
    for a in range(n,0,-1):
        print('*'*a)

'''Pattern 3:
......
****
 ***
  **
   *
   '''
def p3():
    n=int(input("Columns: "))
    for a in range(n,0,-1):
        print(' '*(n-a),'*'*a)

'''Pattern 4:
*
**
* *
*  *
*   *
*  *
* *
**
*
'''
def p4():
    n=int(input("Columns: "))
    print('*')
    for a in range(0,n+1):
        print('*', ' '*a, '*', sep='')
    for a in range(n-1,-1,-1):
        print('*',' '*a, '*', sep='')
    print('*')
