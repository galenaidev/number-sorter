# Number Sorter

A simple command-line application that sorts numbers provided as arguments or from a file.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

There are three ways to provide numbers to the sorter:

1.  **As command-line arguments:**
    ```bash
    python sort_numbers.py 5 2 8 1 9 3
    # Output: 1.0 2.0 3.0 5.0 8.0 9.0
    ```

2.  **From a file (one number per line):**
    Create a file, for example `mynumbers.txt`:
    ```
    5
    2.5
    8
    1
    9.1
    3
    ```
    Then run the script:
    ```bash
    python sort_numbers.py --file mynumbers.txt
    # Or using the short flag:
    # python sort_numbers.py -f mynumbers.txt
    # Output: 1.0 2.5 3.0 5.0 8.0 9.1
    ```

3.  **Via standard input (stdin):**
    ```bash
    echo "5 2 8 1 9 3" | python sort_numbers.py
    # Output: 1.0 2.0 3.0 5.0 8.0 9.0
    ```
    If no arguments or file are provided, the script will wait for input from stdin (press Ctrl-D to end input).

## Features

- Accepts numbers as command-line arguments
- Accepts numbers from a specified file (one number per line)
- Supports input through stdin
- Handles both integers and floating-point numbers
- Provides sorted output in ascending order
