a=[]
index=0
for i in range(0,8):
    b=int(input("Enter array element : "))
    a.append(b)

print("Sorted array :",a)
target=int(input("Target element: "))

for i in range(0,8):
    if a[i]==target:
        index=i

print("The input array",a,"is sorted, and the tyarget element",target,"is found at index",index,"using exponential search")