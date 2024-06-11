num=[]
even=[]
odd=[]
for i in range(1,51,1):
    num.append(i)
    if(i%2==0):
        even.append(i*i)
    else:
        odd.append(i*i)
print("The num list: ")
print(num)
print("\nThe even list: ")
print(even)
print("\nThe odd list: ")
print(odd)

