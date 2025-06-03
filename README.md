# Number Sorter

A simple command-line application that sorts numbers provided as arguments, from a file, or through stdin.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Command-line arguments
```bash
python sort_numbers.py 5 2 8 1 9 3
# Output: 1 2 3 5 8 9
```

### From a file
```bash
python sort_numbers.py -f numbers.txt
# or
python sort_numbers.py --file numbers.txt
```

### Through stdin
```bash
echo "5 2 8 1 9 3" | python sort_numbers.py
```

### Help
```bash
python sort_numbers.py -h
```

## File Format

When using the file input option, the file should contain one number per line:

```
5
2
8
1
9
3
```

Empty lines in the file are ignored.

## Features

- Accepts numbers as command-line arguments
- Supports input from a file (one number per line)
- Supports input through stdin
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order
- Comprehensive error handling for invalid inputs and file errors
