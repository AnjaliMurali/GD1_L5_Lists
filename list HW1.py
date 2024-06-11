marks = [75,36,25,90,58,11,89,69,30]
top=[]
avg=[]
low=[]
for i in marks:
    if i<=30:
        low.append(i)
    elif i<=69:
        avg.append(i)
    elif i>70:
        top.append(i)
low.sort()
avg.sort()
top.sort()
print(low)
print(avg)
print(top)