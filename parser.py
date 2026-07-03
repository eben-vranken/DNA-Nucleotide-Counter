def main(fileName):
    # Read file
    with open(fileName, "r") as f:
        dna_string: str = f.read()

    # Parse and Count
    count_file(dna_string)

def count_file(dna_string: str):
    nucleotide_counts = {
        # Base codes
        # Adenine
        "A": 0,
        # Guanine
        "G": 0,
        # Cytosine
        "C": 0,

        # DNA Specific
        # Thymine
        "T": 0,
        
        # RNA Specific
        # Uracil
        "U": 0,
        
        # Mix codes
        # Adenine or Guanine
        "R": 0,
        # Cytosine or Thymine
        "Y": 0,
        # Guanine or Cytosine
        "S": 0,
        # Adenine or Thymine
        "W": 0,
        # Guanine or Thymine
        "K": 0,
        # Adenine or Cytosine
        "M": 0,
        # Cytosine or Guanine or Thymine
        "B": 0,
        # Adenine or Guanine or Thymine
        "D": 0,
        # Adenine or Cytosine or Thymine
        "H": 0,
        # Adenine or Cytosine or Guanine
        "V": 0,
        
        # Any base
        "N": 0,

        # Gap codes
        ".": 0,
        "-": 0,
    }

    for c in dna_string.upper():
        if c in nucleotide_counts:
            nucleotide_counts[c] += 1

    print(nucleotide_counts)