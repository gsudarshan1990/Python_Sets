#product
a=int(input('Enter the number'))
for i in range(1,11):
    print("{a}*{i}={result}".format(a=a,i=i,result=a*i))

#while loop
i=1
while i<=10:
    print(i)
    i+=1

#Nested Loops
for i in range(1,6):
    print("Level",i,"-",end=" ")
    for j in range(1,11):
        print(j,end=" ")
    print()