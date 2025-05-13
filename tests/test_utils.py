from unittest.mock import patch, mock_open
from src.utils import read_json_file


def test_read_json_file_empty():
    with patch("builtins.open", mock_open(read_data='')):
        result = read_json_file("data/operations.json")
        assert result == []


def test_read_json_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = read_json_file("data/operations.json")
        assert result == []
