
while True:
    n = int(input("Nhập vào một số nguyên dương: "))
    if n < 2:
        print(n, "không phải số nguyên tố")
    else:
        snt=True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                snt = False
                break
        if snt:
            print(n, "là số nguyên tố")
        else:
            print(n, "không phải số nguyên tố")
    hoi = input("Tiếp không(c/k): ")
    if hoi == "k":
        break

