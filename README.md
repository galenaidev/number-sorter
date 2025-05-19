# Number Sorter

A simple command-line application that sorts numbers provided as arguments.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python sort_numbers.py 5 2 8 1 9 3
# Output: 1 2 3 5 8 9

# You can also pipe numbers through stdin
echo "5 2 8 1 9 3" | python sort_numbers.py
# Output: 1 2 3 5 8 9

# You can also provide numbers from a file
# Create a file named 'numbers.txt' with one number per line:
# 5
# 2
# 8
# 1
# 9
# 3
python sort_numbers.py -f numbers.txt
# Output: 1.0 2.0 3.0 5.0 8.0 9.0
```

## Features

- Accepts numbers as command-line arguments
- Supports input through stdin
- Supports input from a file (one number per line) using the -f or --file option.
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order
