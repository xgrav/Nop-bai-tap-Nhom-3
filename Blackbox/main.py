from src.source import check_triangle

if __name__ == "__main__":
    a = float(input("Nhap canh thu nhat: "))
    b = float(input("Nhap canh thu hai: "))
    c = float(input("Nhap canh thu ba: "))

    output = check_triangle(a, b, c)
    print(
        f"Day la ", output)