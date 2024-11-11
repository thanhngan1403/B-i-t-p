s = input("Nhập chuỗi: ")
i = 0 
while  i < len(s):
    if (s[i] == '-' ):
        j = i+1
        number_str1 = ""
        while (j < len(s)):
            if (s[j].isdigit()):
                number_str1 += s[j]
                j+=1
            else: 
                break
        if number_str1:
            print("-" + number_str1)
            i = j
        else:
            i+=1
    else:
        i+=1

