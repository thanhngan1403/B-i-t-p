from random import randrange

def Check_array(arr):
    dem = 0
    for i in range(len(arr)):
        if (arr.count(arr[i]) > 1):
            dem+=1
    return dem == 0
            
#Nhập mảng
n = int(input("Nhập số phần từ: "))
arr=[0]*n
for i in range(n):
    arr[i] = randrange(-100, 100)
if (Check_array(arr)):
    print("Danh sách vừa nhập: ",arr)
else:
    print("Danh sách vừa nhập không hợp lệ: ")
