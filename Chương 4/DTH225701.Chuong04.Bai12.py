def oscillate(start, end):
    result = []
    for i in range(start, end ):
        if i !=0 or i==0:
            result.append(i)
            result.append(-i)
        else:
            result.append(i)
    return result

# Sử dụng hàm oscillate và in kết quả
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
