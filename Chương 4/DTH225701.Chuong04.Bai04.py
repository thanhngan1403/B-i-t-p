def ROI(dt,cp):
    return (dt-cp)/cp
def Goiydautu(roi):
    if roi>=0.75:
        return "Nên đầu tư"
    else:
        return "không đầu tư"
dt=int(input("nhập danh thu: "))
cp=int(input("nhập chi phí: "))
roi=ROI(dt,cp)
print("tỉ lệ roi=",roi)
print(" ",Goiydautu(roi))

    
