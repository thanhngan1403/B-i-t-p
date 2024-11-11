from random import randrange

#Nhập mảng
n = int(input("Nhập số phần từ: "))
arr=[0]*n
for i in range(n):
    arr[i] = randrange(-100, 100)
print("Danh sách vừa nhập: ",arr)

#Nhập số cần xóa
k = int(input("Nhập phần từ cần xóa: "))
if (arr.count(k) == 0):
    print("{0} không có trong mảng".format(k))
else:
    arr.remove(k)
    print("Danh sách sau khi xóa {0}: ".format(k), arr)

if (arr == arr[::-1]):
    print("Đây là mảng đối xứng")
else:
    print("Đây là mảng không đối xứng")