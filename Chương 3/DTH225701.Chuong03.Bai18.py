n = int(input("Nhap n:"))
print("Hinh 1")
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHinh 2")
for i in range(n):
    for j in range(n):
        if j >= (n-1)-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHinh3")
center = n//2
for i in range(n):
    for j in range(n):
        if i <= center:
            if(j==0 or i==j or i==center):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if(i==j or j==(n-1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

