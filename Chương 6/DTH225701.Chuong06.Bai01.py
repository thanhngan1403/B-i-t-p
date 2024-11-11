from random import randrange

def KTR_SNT(number):
    dem = 1
    for i in range(2, number):
        if (number % i == 0):
            dem+=1
    return (dem == 1 and number > 0 and number != 1)

def Tong_SNT(list, n):
    s = 0
    for i in range(0, n):
        if (KTR_SNT(list[i])):
            s += list[i]
    return s

n = int(input("Nhập số phần từ: "))
list=[0]*n
for i in range(n):
    list[i] = randrange(-100, 100)
print("Danh sách vừa nhập: ",list)

x = int(input("Nhập phần tử cần thêm: "))
list.append(x)
n+=1
print("Danh sách sau khi thêm {0}: ".format(x),list)

k = int(input("Nhập phần từ cần đếm: "))
print("Số lần xuất hiện của {0}: {1}".format(k, list.count(k)))

print("Tổng các số nguyên tố: {0}".format(Tong_SNT(list, n)))
list.sort()
print("Danh sách sau khi sắp xếp: ", list)

del list
print("Danh sách sau khi xóa: ", list)

