def read_file(fileName):
    # Read file
    with open(fileName, "r") as f:
        dna_string: str = f.read()

    # Parse and Count
    return dna_string

def count_nucleotides(dna_string: str):
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
        # Cytosine or Thymine (or Uracil)
        "Y": 0,
        # Guanine or Cytosine
        "S": 0,
        # Adenine or Thymine (or Uracil)
        "W": 0,
        # Guanine or Thymine (or Uracil)
        "K": 0,
        # Adenine or Cytosine
        "M": 0,
        # Cytosine or Guanine or Thymine (or Uracil)
        "B": 0,
        # Adenine or Guanine or Thymine (or Uracil)
        "D": 0,
        # Adenine or Cytosine or Thymine (or Uracil)
        "H": 0,
        # Adenine or Cytosine or Guanine
        "V": 0,
        
        # Any base
        "N": 0,

        # Gap codes
        ".": 0,
        "-": 0,
    }

    cleaned_string = "".join(dna_string.split())
    for c in cleaned_string.upper():
        if c in nucleotide_counts:
            nucleotide_counts[c] += 1
        else:
            print("Unknown symbol: %s" % c)
    return nucleotide_counts

def calculate_gc(nucleotide_counts):
    return 100*(nucleotide_counts["G"] + nucleotide_counts["C"])/(nucleotide_counts["A"] + nucleotide_counts["C"] + nucleotide_counts["G"] + nucleotide_counts["T"])