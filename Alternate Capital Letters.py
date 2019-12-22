str=input("String: ").lower() #accepting string in lower case
str2=str[0].upper() #storing first letter of str1 in upper case
for i in range(1, len(str)):
    if str2[i-1].isupper():
        str2 += str[i]
    elif str2[i-1].islower():
        str2 += str[i].upper()
    elif str2[i-1].isspace():
        str2 += str[i].upper()
print(str2)
