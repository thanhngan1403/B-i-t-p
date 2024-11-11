n = int(input("Nhập số phần từ: "))
arr=[0]*n
for i in range(n):
    arr[i] = float(input("a[{0}]=".format(i+1)))
arr.sort()
print("Mảng số thực sau khi sắp xếp: ", arr[::-1])