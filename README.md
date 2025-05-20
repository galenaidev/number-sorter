# Number Sorter

A simple command-line application that sorts numbers provided as arguments, from a file, or via stdin.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Via Command-Line Arguments
```bash
python sort_numbers.py 5 2 8 1 9 3
# Output: 1.0 2.0 3.0 5.0 8.0 9.0
```

### Via File Input
Create a file (e.g., `numbers.txt`) with one number per line:
```
10
5
20
1
15
```
Then run the script:
```bash
python sort_numbers.py -f numbers.txt
# Output: 1.0 5.0 10.0 15.0 20.0
```

### Via Standard Input (stdin)
```bash
echo "5 2 8 1 9 3" | python sort_numbers.py
# Output: 1.0 2.0 3.0 5.0 8.0 9.0
```

## Features

- Accepts numbers as command-line arguments
- Accepts numbers from a file (one number per line) using the `-f` or `--file` option.
- Supports input through stdin
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order
