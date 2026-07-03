import unittest
from unittest.mock import patch, mock_open
import compiler

class TestCompilerIO(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_output_writes_to_correct_file_path(self, mock_file):
        """Ensure compiler writes to the correctly formatted file path string."""
        mock_counts = {"A": 10, "G": 5}
        
        compiler.output(mock_counts, "json", "results/my_output")
        
        mock_file.assert_called_once_with("results/my_output.json", 'w')
        
        handle = mock_file()
        handle.write.assert_called_once_with('{\n    "A": 10,\n    "G": 5\n}')

    @patch('builtins.open', new_callable=mock_open)
    def test_output_writes_csv_content(self, mock_file):
        mock_counts = {"A": 10, "G": 5}

        compiler.output(mock_counts, "csv", "results/my_output")

        mock_file.assert_called_once_with("results/my_output.csv", 'w')

        handle = mock_file()
        handle.write.assert_called_once_with('A,G\r\n10,5\r\n')

    @patch('builtins.open', new_callable=mock_open)
    def test_output_writes_txt_content(self, mock_file):
        mock_counts = {"A": 10, "G": 5}

        compiler.output(mock_counts, "txt", "results/my_output")

        mock_file.assert_called_once_with("results/my_output.txt", 'w')

        handle = mock_file()
        handle.write.assert_called_once_with('A: 10\nG: 5')

if __name__ == "__main__":
    unittest.main()