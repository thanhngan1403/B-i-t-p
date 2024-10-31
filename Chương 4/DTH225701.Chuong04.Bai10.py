import time

# Vẽ hình 1
def draw_1(n):
    # Vẽ phần trên
    for i in range(1, n + 1):
        if i == n:
            # Vẽ hàng giữa
            print("* " * (2 * n -1))
        else:
            print("  " * (n -1) + "* "* i)
    # Vẽ phần dưới
    for i in range(1, n):
        print("* " * (n - i))

# Vẽ hình 2
def draw_2(n):
    # Vẽ phần trên
    for i in range(1, n + 1):
        if i == n:
            # Vẽ hàng giữa
            print("* " * (2 * n - 1))
        elif i > 2:
            print("  " * (n-1) + "* " + " " * (2 * (i - 1) - 2) + "*" )
        else:
            print("  " * (n-1) + "* " * i)

    # Vẽ phần dưới
    for i in range(n-1, 0, -1):
        if i > 2:
            print("* " + " " * (2 * (i - 1) - 2) + "*")
        else:
            print("* " * i)

# Vẽ hình 3
def draw_3(n):
    # Vẽ phần trên
    for i in range(1, n + 1):
        print("  " * (n-1) + "* " * (n - i + 1))
    # Vẽ phần dưới
    for i in range(n-1, 0, -1):
        print("  " * (i - 1) + "* " * (n + 1 - i))

# Vẽ hình 4
def draw_4(n):
    # Vẽ phần trên
    for i in range(1, n + 1):
        if (i > 1 and i < n - 1):
             print("  " * (n-1) + "* " + "  " * (n - i - 1) + "*" )
        else:
            print("  " * (n-1) + "* " * (n - i + 1))
    # Vẽ phần dưới
    for i in range(n-1, 0, -1):
        if (i > 1 and i < n):
            print("  " * (i - 1) + "* " + "  " *(n - i - 1) + "*" )
        else:
            print("  " * (i - 1) + "* " * (n + 1 - i))


# Gọi hàm với chiều dài cạnh n
n = int(input("Nhập chiều dài cạnh: "))
print("Hình 1: \n")
draw_1(n)
time.sleep(0.5)
print("\nHình 2: \n")
draw_2(n)
time.sleep(0.5)
print("\nHình 3: \n")
draw_3(n)
time.sleep(0.5)
print("\nHình 4: ")
draw_4(n)
