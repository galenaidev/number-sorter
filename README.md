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
```

## Features

- Accepts numbers as command-line arguments
- Supports input through stdin
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order
