#XuLyFile.py
def LuuFile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()
def DocFile(path):
    arrProduct=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        arr=data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct

#TestDocFile.py
# from XuLyFile import *
dssp=DocFile(r"D:\python\B-i-t-p\Chương 7\database.txt")
#print(dssp)
def XuatSanPham(dssp):
    for row in dssp:
        for element in row:
            print(element,end='\t')
        print()
    print()
XuatSanPham(dssp)
def SortSp(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a=dssp[i]
            b=dssp[j]
            if a[2]>b[2]:
                dssp[i]=b
                dssp[j]=a
SortSp(dssp)
print("Sản phẩm sau khi sắp xếp giá:")
XuatSanPham(dssp)

#TestLuuFile.py
# from XuLyFile import *
masp=input("nhập mã SP:")
tensp=input("nhập tên sp:")
dongia=float(input("nhập giá:"))
#xuong dong moi
line="\n" + masp + ";" + tensp + ";" + str(dongia)
LuuFile(r"D:\python\B-i-t-p\Chương 7\database.txt",line)