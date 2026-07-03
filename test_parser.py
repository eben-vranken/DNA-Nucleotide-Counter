import unittest
import tempfile
from pathlib import Path
from parser import count_nucleotides
from parser import read_file

class TestNucleotideCounter(unittest.TestCase):

    def test_standard_dna_counts(self):
        """Test that standard DNA bases are counted accurately."""
        sequence = "AGCTAGCT"
        counts = count_nucleotides(sequence)
        self.assertEqual(counts["A"], 2)
        self.assertEqual(counts["G"], 2)
        self.assertEqual(counts["C"], 2)
        self.assertEqual(counts["T"], 2)
        self.assertEqual(counts["U"], 0)

    def test_case_insensitivity(self):
        """Test that lowercase inputs are automatically converted and counted."""
        sequence = "agct"
        counts = count_nucleotides(sequence)
        self.assertEqual(counts["A"], 1)
        self.assertEqual(counts["T"], 1)

    def test_ambiguity_and_gaps(self):
        """Test that IUPAC mixed codes, ambiguity codes, and gaps are registered."""
        sequence = "RNS-"
        counts = count_nucleotides(sequence)
        self.assertEqual(counts["R"], 1)
        self.assertEqual(counts["N"], 1)
        self.assertEqual(counts["S"], 1)
        self.assertEqual(counts["-"], 1)
        self.assertEqual(counts["."], 0)

    def test_empty_sequence(self):
        """Test that an empty string returns all zeroes cleanly."""
        counts = count_nucleotides("")
        self.assertTrue(all(count == 0 for count in counts.values()))

    def test_read_file_returns_file_contents(self):
        """Test that parser.read_file reads the exact file content from disk."""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "example.txt"
            file_path.write_text("AaTt\nRNS", encoding="utf-8")

            self.assertEqual(read_file(str(file_path)), "AaTt\nRNS")

if __name__ == "__main__":
    unittest.main()