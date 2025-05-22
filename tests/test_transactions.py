import unittest
from unittest.mock import patch
import pandas as pd
from src.transactions import read_transactions_from_csv, read_transactions_from_excel


class TestTransactionReading(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_transactions_from_csv(self, mock_read_csv):
        # Настройка mock объекта
        mock_data = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02'],
            'amount': [100, 200],
            'description': ['Deposit', 'Withdrawal']
        })
        mock_read_csv.return_value = mock_data

        result = read_transactions_from_csv('dummy_path.csv')

        expected_result = [
            {'date': '2023-01-01', 'amount': 100, 'description': 'Deposit'},
            {'date': '2023-01-02', 'amount': 200, 'description': 'Withdrawal'}
        ]

        self.assertEqual(result, expected_result)

    @patch('pandas.read_excel')
    def test_read_transactions_from_excel(self, mock_read_excel):
        # Настройка mock объекта
        mock_data = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02'],
            'amount': [150, 250],
            'description': ['Transfer', 'Deposit']
        })
        mock_read_excel.return_value = mock_data

        result = read_transactions_from_excel('dummy_path.xlsx')

        expected_result = [
            {'date': '2023-01-01', 'amount': 150, 'description': 'Transfer'},
            {'date': '2023-01-02', 'amount': 250, 'description': 'Deposit'}
        ]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
