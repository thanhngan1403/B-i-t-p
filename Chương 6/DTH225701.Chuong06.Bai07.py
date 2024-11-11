def check_arr(arr):
    for i in range(0, len(arr)-1): 
        if arr[i] > arr[i + 1]:
            return True
    return False

#Nhập mảng
n = int(input("Nhập số phần từ: "))
arr=[0]*n
for i in range(n):
    arr[i] = int(input("a[{0}]=".format(i+1)))
while (check_arr(arr)):
    print("Bạn nhập mảng sai quy cách!!!")
    print("Vui lòng nhập lại các phần tử")
    arr=[0]*n
    for i in range(n):
        arr[i] = int(input("a[{0}]=".format(i+1)))
print("Mảng vừa nhập: ", arr)

