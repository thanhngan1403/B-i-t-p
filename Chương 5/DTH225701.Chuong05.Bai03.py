def KtrSNT(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    return dem == 2

s = input("Nhập chuỗi: ")
arr = s.split(';')
sochan = 0
soam = 0
snt = 0
tb = 0
for i in arr:
    number = int(i)
    print(number)
    if number % 2 == 0:
        sochan+=1
    if number < 0:
        soam+=1
    if KtrSNT(number):
        snt+=1
    tb += number

print("Có ",sochan," số chẵn")
print("\nCó ",soam,"số âm")
print("\nCó ",snt," số nguyên tố")
print("\nGiá trị trung bình: ",tb/len(arr))