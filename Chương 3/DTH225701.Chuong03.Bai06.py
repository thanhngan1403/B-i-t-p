# Nhập số n
n = int(input("Nhập số n (tối đa 2 chữ số): "))
def doc_so(n): #định nghĩa hàm 
    hang_don_vi = [ "", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    if n < 10:
        return hang_don_vi[n]
    else:
        chuc = n // 10
        don_vi = n % 10
        if don_vi == 0:
            return hang_chuc[chuc]
        elif don_vi == 5:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + hang_don_vi[don_vi]
print(doc_so(n))

