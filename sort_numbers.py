#!/usr/bin/env python3

import sys
import argparse

def read_numbers_from_file(filepath):
    """Reads numbers from a file, one number per line."""
    numbers = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line: # Ensure line is not empty
                    numbers.append(float(line))
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print(f"Error: File contains non-numeric data: {filepath}", file=sys.stderr)
        sys.exit(1)
    return numbers

def main():
    parser = argparse.ArgumentParser(description="Sort numbers provided via arguments, a file, or stdin.")
    parser.add_argument('numbers_cli', nargs='*', type=float, help="Numbers to sort, provided as arguments.")
    parser.add_argument('-f', '--file', type=str, help="Path to a file containing numbers, one per line.")
    
    args = parser.parse_args()
    
    numbers = []

    try:
        if args.file:
            numbers = read_numbers_from_file(args.file)
        elif args.numbers_cli:
            numbers = args.numbers_cli
        else:
            # Correctly indented block for stdin
            print("No file or direct arguments provided. Reading from stdin (Ctrl-D to end):", file=sys.stderr)
            input_lines = sys.stdin.readlines()
            for line in input_lines:
                stripped_line = line.strip()
                if stripped_line: 
                    try:
                        numbers.extend([float(num) for num in stripped_line.split()])
                    except ValueError:
                        print(f"Error: Invalid input in stdin. Please provide valid numbers.", file=sys.stderr)
                        sys.exit(1)
        
        if not numbers:
            print("Error: No numbers provided. Use arguments, --file option, or stdin.", file=sys.stderr)
            sys.exit(1)
        
        sorted_numbers = sorted(numbers)
        print(" ".join(str(num) for num in sorted_numbers))
        
    except ValueError: 
        print(f"Error: Invalid input. Please provide valid numbers as arguments.", file=sys.stderr)
        sys.exit(1)
    # FileNotFoundError and file-related ValueErrors are handled in read_numbers_from_file

if __name__ == "__main__":
    main()
