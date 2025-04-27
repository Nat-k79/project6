import pytest
from processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"state": "active", "date": "2023-01-01"},
        {"state": "inactive", "date": "2022-12-31"},
        {"state": "active", "date": "2023-01-02"},
    ]


def test_filter_by_state(sample_data):
    assert filter_by_state(sample_data, "active") == [
        {"state": "active", "date": "2023-01-01"},
        {"state": "active", "date": "2023-01-02"},
    ]
    assert filter_by_state(sample_data, "inactive") == [
        {"state": "inactive", "date": "2022-12-31"},
    ]
    assert filter_by_state(sample_data, "nonexistent") == []


@pytest.mark.parametrize("order, expected_dates", [
    ("asc", ["2022-12-31", "2023-01-01", "2023-01-02"]),
    ("desc", ["2023-01-02", "2023-01-01", "2022-12-31"]),
])
def test_sort_by_date(sample_data, order, expected_dates):
    sorted_data = sort_by_date(sample_data, order)
    assert [item["date"] for item in sorted_data] == expected_dates
