from argparse import ArgumentParser
import parser
import compiler
import sys

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

    try:
        nucleic_acid_string = parser.read_file(args.file)
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' could not be found.", file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{args.file}'.", file=sys.stderr)
        exit(1)
    nucleotide_counts = parser.count_nucleotides(nucleic_acid_string)
    
    # Sanitize based on mode
    if args.mode == "dna":
        nucleotide_counts.pop("U", None)
    else:
        nucleotide_counts.pop("T", None)

    # Merge gap
    dot_count = nucleotide_counts.pop(".", None)
    dash_count = nucleotide_counts.pop("-", None)
    nucleotide_counts["Gap"] = dot_count + dash_count

    if args.output:
        compiler.output(nucleotide_counts, args.format, args.output)
    else:
        TABLE_WIDTH = 38

        print("=" * TABLE_WIDTH)
        print(f"{'Genomic Summary':^38}")
        print("=" * TABLE_WIDTH)

        print(f"Sequence Type: {args.mode.upper():>23}")
        print(f"Bases Count:   {sum(nucleotide_counts.values()):>23}")
        print("=" * TABLE_WIDTH)
        labels = {
            "A": "Adenine", "G": "Guanine", "C": "Cytosine", "T": "Thymine", "U": "Uracil",
            "R": "A or G", "Y": "C or T/U", "S": "G or C", "W": "A or T/U", "K": "G or T/U",
            "M": "A or C", "B": "C or G or T/U", "D": "A or G or T/U", "H": "A or C or T/U",
            "V": "A or C or G", "N": "Any base", "Gap": "Gap"
        }

        total = sum(nucleotide_counts.values())

        for symbol, label in labels.items():
            count = nucleotide_counts.get(symbol, 0)
            percent = (count / total * 100) if total else 0
            
            # Formatting Breakdown:
            # {label:<15}  -> Left-align label in a 15-character column
            # {symbol:^3}   -> Center-align symbol in a 3-character column
            # {count:>5}    -> Right-align count in a 5-character column
            # {percent:>5.1f} -> Right-align percentage with 1 decimal place in a 5-character column
            print(f"{label:<15} ({symbol:^3}): {count:>5}  ({percent:>5.1f}%)")