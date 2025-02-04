
str1 = ""

i=0
while i < 6:
    i+=1
    for j in range(1,i+1):
        str1+=str(j)
    str1+=" "
    for k in range(6+1-i, 0, -1):
        str1+=str(k)
    print(str1)
    str1=""