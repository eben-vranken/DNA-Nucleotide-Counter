import unittest
from io import StringIO
import sys
from parser import count_nucleotides

class TestParserEdgeCases(unittest.TestCase):

    def test_unknown_symbol_handling(self):
        """Ensure invalid symbols are skipped and print an alert message."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        sequence = "ACGTZ"
        counts = count_nucleotides(sequence)
        
        sys.stdout = sys.__stdout__
        
        self.assertIn("Unknown symbol: Z", captured_output.getvalue())
        self.assertEqual(counts["A"], 1)

if __name__ == "__main__":
    unittest.main()