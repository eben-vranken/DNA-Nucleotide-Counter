import json
import io
import csv

def output(nucleotide_count: dict[str, int], args):
    file_location = args.output
    format = args.format

    file = build_file(format, nucleotide_count)

    file_path: str

    file_path = file_location + "." + format

    with open(file_path, 'w') as fp:
        fp.write(file)

def build_file(format, nucleotide_count):
    match format:
        case "json":
            return json_output(nucleotide_count)
        case "csv":
            return csv_output(nucleotide_count)
        case "txt":
            return txt_output(nucleotide_count)
        
def json_output(nucleotide_count):
    return json.dumps(nucleotide_count, indent=4)

def csv_output(nucleotide_count):
    buffer = io.StringIO()
    writer = csv.writer(buffer)

    writer.writerow(nucleotide_count.keys())
    writer.writerow(nucleotide_count.values())

    return buffer.getvalue()

def txt_output(nucleotide_count):
    return "\n".join(f"{base}: {count}" for base, count in nucleotide_count.items())