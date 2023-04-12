def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Khong phai tam giac"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Khong phai tam giac"
    elif a == b and b == c:
        return "Tam giac deu"
    elif a == b or b == c or a == c:
            return "Tam giac can"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Tam giac vuong"
    else:
        return "Tam giac thuong"

