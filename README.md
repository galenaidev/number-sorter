# Number Sorter

A simple command-line application that sorts numbers provided as arguments or from a file.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Sort numbers provided as arguments
python sort_numbers.py 5 2 8 1 9 3
# Output: 1 2 3 5 8 9

# Sort numbers from a file (one number per line)
python sort_numbers.py -f numbers.txt

# You can also pipe numbers through stdin
echo "5 2 8 1 9 3" | python sort_numbers.py
```

## Features

- Accepts numbers as command-line arguments
- Supports reading numbers from a file (one number per line)
- Supports input through stdin
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order

## File Input Format

When using the `-f` or `--file` option, the input file should contain one number per line. For example:

```
5
2
8.5
1
9
3.14
```

Empty lines in the file are ignored.
