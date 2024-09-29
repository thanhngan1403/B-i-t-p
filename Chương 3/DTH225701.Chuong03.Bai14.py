a=0
while a<100:
    b=0
    while b<40:
        if(a+b)%2==0:
            print('*',end=' ')
        b+=1
    print()
    a+=1
"""
Vòng lặp ngoài: a chạy từ 0 đến 99 (100 lần).
Vòng lặp trong: b chạy từ 0 đến 39 (40 lần).

Điều kiện để in dấu * là (a + b) % 2 == 0, tức là tổng của a và b phải là số chẵn.

Khi a là số chẵn, b phải là số chẵn để (a + b) là số chẵn.
Khi a là số lẻ, b phải là số lẻ để (a + b) là số chẵn.

Trong mỗi vòng lặp của a, có 20 giá trị của b (từ 0 đến 39) thỏa mãn điều kiện (a + b) % 2 == 0.
Vì a chạy từ 0 đến 99 (100 lần), và mỗi lần có 20 giá trị của b thỏa mãn điều kiện, tổng số dấu * được in ra là:
100×20=2000
Vậy, có 2000 dấu * được in ra trên màn hình từ đoạn mã trên"""