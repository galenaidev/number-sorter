# Number Sorter

A simple command-line application that sorts numbers provided as arguments, through stdin, or from a file.

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

### Input through stdin
```bash
echo "5 2 8 1 9 3" | python sort_numbers.py
# Output: 1 2 3 5 8 9
```

### Input from file
```bash
# Create a file with numbers (one per line)
echo -e "5\n2\n8\n1\n9\n3" > numbers.txt

# Sort numbers from file
python sort_numbers.py --file numbers.txt
# or
python sort_numbers.py -f numbers.txt
# Output: 1 2 3 5 8 9
```

### Help
```bash
python sort_numbers.py --help
```

## Features

- Accepts numbers as command-line arguments
- Supports input through stdin
- **NEW:** Supports reading numbers from a file (one number per line)
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order
- Error handling for invalid numbers and file operations
- Skips empty lines in input files
