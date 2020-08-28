import pytest

from csv_parser import parse


@pytest.mark.parametrize('csv_data, expected', [
    (
        "1, 2, 3\n4, 5, 6\n7, 8, 9\n",
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ),   
    (
        "1, 2, 3\n4, 5, 6\n7, 8, 9",
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ),
    (
        "10, 21, 32\n43, 54, 65\n76, 87, 98",
        [[10, 21, 32],[43, 54, 65], [76, 87, 98]],
    ),
    # (
        # "\n 1, \n 2, 3 \n 4, 5, 6",
        # [[], [1], [2, 3], [4, 5, 6]]
    # ),
])
def test_parse_int_array(csv_data, expected):
    assert parse(csv_data) == expected 


@pytest.mark.parametrize('csv_data, expected', [
    (
        "3.14, 2.159\n 4.00, 5.01",
        [[3.14, 2.159], [4.00, 5.01]]
    )
])
def test_parse_float_array(csv_data, expected):
    assert parse(csv_data) == expected

@pytest.mark.xfail
def parse_empty_fields():
    data = ", 2, 3\n4, , 6\n7, 8, "
    assert parse(data) == [[None, 2, 3], [4, None, 6], [7, 8, None]]
