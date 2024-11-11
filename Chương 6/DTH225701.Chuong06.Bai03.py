from random import randrange

def TaoMaTran(m, n):
    D=[]
    for i in range(m):
        C=[]
        for j in range(n):
            C.append(randrange(0,100))
        D.append(C)
    return D

#Xuất ma trận
def XuatMaTran(D):
    for i in D:
        for j in i:
            print(j, end = "\t")
        print()

#In dòng
def InDong(D, k):
    return D[k-1]

#In cột
def InCot(D, k):
    C =[]
    for i in range(len(D)):
        C.append(D[i][k-1])
    return C

#Max
def Max(D):
    max = D[0][0]
    for i in D:
        for j in i:
            if max < j:
                max = j
    return max

#Nhập ma trận
arr=[]
m = int(input("Nhập số dòng ma trận: "))
n = int(input("Nhập số cột ma trận: "))
arr=TaoMaTran(m,n)
XuatMaTran(arr)

d = int(input("Nhập số dòng cần in: "))
#Dòng cần in
if d > m:
    print("Số dòng nhập không hợp lệ")
else:
    print("Dòng cần in: ", InDong(arr, d))

#Cột cần in
c = int(input("Nhập số cột cần in: "))
if c > n:
    print("Số cột nhập không hợp lệ")
else:
    print("Dòng cần in: ", InCot(arr, c))

#Giá trị lớn nhất
print("Giá trị lớn nhất am trận: {0}".format(Max(arr)))


    