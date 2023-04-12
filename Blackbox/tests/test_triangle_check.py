import pytest
from src.source import check_triangle

@pytest.mark.parametrize(
    "a, b, c, output",
    [(3, 3, 3, "Tam giac deu"),
     (3, 4, 5, "Tam giac vuong"),
     (3, 3, 4, "Tam giac can"),
     (2, 2, 5, "Khong phai tam giac"),
     (1, 2, 3, "Khong phai tam giac"),
     (-1, 2, 3, "Khong phai tam giac"),
     (0, 0, 0, "Khong phai tam giac")
    ],
)
def test_check_triangle(a, b, c, output):
    assert check_triangle(a, b, c) == output
