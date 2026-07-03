<h1 align="center">🧬 Nucleotide Counter</h1>

<p align="center">
    A robust command-line utility to count and categorize DNA/RNA nucleotides, IUPAC ambiguity codes, and gaps with full test coverage.
</p>

<p align="center">
    <a href="#"><img src="https://img.shields.io/badge/Coverage- 94%25-brightgreen.svg" alt="Coverage"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License"></a>
    <a href="https://github.com/eben-vranken/nucleotide-counter/actions">
    <img src="https://github.com/eben-vranken/nucleotide-counter/actions/workflows/test.yml/badge.svg" alt="Build Status">
    </a>
</p>

A modular, zero-dependency Python CLI built to parse genomic sequence strings. Unlike basic string tally tools, it cleans raw sequence data, evaluates complex IUPAC mixed/ambiguity bases, detects sequence gaps, handles mode sanitization (DNA vs. RNA), and exports structured reports.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/nucleotide-counter.git
cd nucleotide-counter
```

## Usage

Pass a text file containing a raw genomic sequence. By default, it processes DNA mode and outputs a beautiful summary directly to the terminal.

```bash
python cli.py sequence.txt --mode dna
```

### Save Output Report

Export your analysis results into multiple structured standard data formats using the `--output` and `--format` options:

```bash
python cli.py sequence.txt --mode rna --format json --output report
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `file` | *Positional path string* | *Required* | Path to the input file containing raw genomic text. |
| `--mode` | `dna`, `rna` | `dna` | Sets sequence rules (automatically drops opposing T/U bases). |
| `--format` | `json`, `csv`, `txt` | `json` | Structural serialization standard for saving metrics. |
| `--output` | *Filepath destination* | `None` | Cleans and compiles data directly into a dedicated report file. |

## Feature Set

* **IUPAC Alphabet Compliant:** Counts individual base elements alongside standard ambiguous codes (`R`, `Y`, `S`, `W`, `K`, `M`, `B`, `D`, `H`, `V`, `N`).
* **Gap Consolidation:** Seamlessly identifies, counts, and merges gap notation elements (`.` and `-`) into a combined metric track.
* **Stream Sanitization:** Strips stray carriage returns, spaces, and linebreaks from the file on-the-fly without corrupting metric balances.

## Testing

Run the automated test suite to verify parsing logic accuracy, compiler formatting integrity, and CLI edge-case execution pipelines:

```bash
python -m unittest discover
```

### Coverage Report

To review full execution trace line metrics:

```bash
python -m coverage run -m unittest discover
python -m coverage report -m
```

## License

MIT
