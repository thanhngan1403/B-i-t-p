def ktrDoiXung(str):
    ktr = str[::-1]
    if (ktr == str):
        return True
    return False

while True:
    s = input("Nhập 1 chuỗi: ")
    if (ktrDoiXung(s)):
        print("Chuỗi bạn nhập đối xứng ")
    else:
        print("Chuỗi bạn không nhập đối xứng ")
    chon = input("Bạn có muốn tiếp tục không (c/k): ")
    if (chon == "k"):
        break;

