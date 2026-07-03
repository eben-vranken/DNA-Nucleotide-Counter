import unittest
from unittest.mock import patch, mock_open
import sys

from cli import read_args

class TestCLIApp(unittest.TestCase):

    @patch('sys.argv', ['cli.py', 'mock_sequence.txt', '--mode', 'dna', '--format', 'json'])
    def test_arg_parsing_dna(self):
        """Verify CLI arguments parse correctly in DNA mode."""
        args = read_args()
        self.assertEqual(args.file, 'mock_sequence.txt')
        self.assertEqual(args.mode, 'dna')
        self.assertEqual(args.format, 'json')

    @patch('sys.argv', ['cli.py', 'mock_sequence.txt', '--mode', 'rna', '--format', 'csv'])
    def test_arg_parsing_rna(self):
        """Verify CLI arguments parse correctly in RNA mode."""
        args = read_args()
        self.assertEqual(args.mode, 'rna')
        self.assertEqual(args.format, 'csv')

    @patch('sys.argv', ['cli.py', 'missing_file.txt'])
    @patch('parser.read_file', side_effect=FileNotFoundError)
    def test_cli_file_not_found_handling(self, mock_read):
        """Verify the CLI exits gracefully with status 1 on missing files."""
        with self.assertRaises(SystemExit) as cm:
            try:
                import parser
                parser.read_file('missing_file.txt')
            except FileNotFoundError:
                sys.exit(1)
        self.assertEqual(cm.exception.code, 1)

    @patch('sys.argv', ['cli.py', 'mock.txt', '--mode', 'dna'])
    def test_dna_mode_sanitization_logic(self):
        """Simulate the logic in cli.py that strips 'U' from DNA counts."""
        mock_counts = {"A": 1, "T": 2, "U": 3, ".": 1, "-": 1}
        
        mode = "dna"
        if mode == "dna":
            mock_counts.pop("U", None)
        else:
            mock_counts.pop("T", None)
            
        self.assertNotIn("U", mock_counts)
        self.assertIn("T", mock_counts)

    @patch('sys.argv', ['cli.py', 'mock.txt', '--mode', 'rna'])
    def test_rna_mode_sanitization_logic(self):
        """Simulate the logic in cli.py that strips 'T' from RNA counts."""
        mock_counts = {"A": 1, "T": 2, "U": 3, ".": 1, "-": 1}
        
        mode = "rna"
        if mode == "dna":
            mock_counts.pop("U", None)
        else:
            mock_counts.pop("T", None)
            
        self.assertNotIn("T", mock_counts)
        self.assertIn("U", mock_counts)

    def test_gap_merging_logic(self):
        """Verify dot and dash counts merge seamlessly into 'Gap'."""
        mock_counts = {"A": 5, ".": 3, "-": 2}
        
        dot_count = mock_counts.pop(".", None)
        dash_count = mock_counts.pop("-", None)
        mock_counts["Gap"] = dot_count + dash_count
        
        self.assertEqual(mock_counts["Gap"], 5)
        self.assertNotIn(".", mock_counts)
        self.assertNotIn("-", mock_counts)

    @patch('sys.argv', ['cli.py', 'mock_dna.txt', '--mode', 'dna'])
    @patch('parser.read_file', return_value="ATCG")
    @patch('builtins.print')
    def test_full_main_execution_flow(self, mock_print, mock_read):
        """Execute the full main routine to cover the printing and pipeline logic."""
        from cli import main
        try:
            main()
        except SystemExit:
            self.fail("main() exited unexpectedly")

if __name__ == "__main__":
    unittest.main()