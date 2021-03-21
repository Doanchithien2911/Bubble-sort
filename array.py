from bubblesort import bubble_sort
n=int(input("nhap so phan tu cua mang : "))
if n<=0:
    exit()
arr=[]
for i in range(0,n):
    x=int(input("nhap gia tri cho phan tu thu %d " % (i) ))
    arr.append(x)
print("mang da tao la :")
print(arr)
print("mang sau khi sap xep la :")
print(bubble_sort(arr))    
        
    