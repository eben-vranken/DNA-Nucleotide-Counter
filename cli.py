from argparse import ArgumentParser
import parser

def read_args():
    parser = ArgumentParser()
    parser.add_argument("file", help="Data file to read")

    # Optional arguments
    parser.add_argument("--mode", choices=["dna", "rna"], default="dna", help="Analysis mode (dna/rna)")
    parser.add_argument("--format", choices=["json", "csv", "txt"], default="json", help="Output format (json/csv/txt)")
    parser.add_argument("--output", help="Output file path")

    return parser.parse_args()

if  __name__ == "__main__":
    args = read_args()
    nucleic_acid_string = parser.read_file(args.file)
    nucleotide_count = parser.count_nucleotides(nucleic_acid_string)
    
    if args.mode == "dna":
        nucleotide_count.pop("U", None)
    else:
        nucleotide_count.pop("T", None)

    print(nucleotide_count)