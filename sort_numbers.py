#!/usr/bin/env python3

import sys
import argparse

def read_numbers_from_file(filename):
    """Read numbers from a file, one number per line."""
    try:
        with open(filename, 'r') as f:
            numbers = []
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"Error: Invalid number '{line}' on line {line_num} in file '{filename}'")
                        sys.exit(1)
            return numbers
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

def get_numbers_from_args(args):
    """Get numbers from command line arguments."""
    return [float(arg) for arg in args]

def get_numbers_from_stdin():
    """Get numbers from stdin."""
    try:
        input_line = sys.stdin.readline().strip()
        return [float(num) for num in input_line.split()]
    except EOFError:
        return []

def main():
    parser = argparse.ArgumentParser(description='Sort numbers in ascending order')
    parser.add_argument('--file', '-f', type=str, help='Read numbers from file (one number per line)')
    parser.add_argument('numbers', nargs='*', type=float, help='Numbers to sort (if not using --file)')
    
    args = parser.parse_args()
    
    try:
        # Get numbers based on input method
        if args.file:
            # Read from file
            numbers = read_numbers_from_file(args.file)
        elif args.numbers:
            # Use command line arguments
            numbers = args.numbers
        else:
            # Read from stdin
            numbers = get_numbers_from_stdin()
        
        if not numbers:
            print("Error: No numbers provided. Please provide numbers as arguments, through stdin, or via a file.")
            parser.print_help()
            sys.exit(1)
        
        # Sort the numbers
        sorted_numbers = sorted(numbers)
        
        # Print the sorted numbers
        print(" ".join(str(num) for num in sorted_numbers))
        
    except ValueError as e:
        print(f"Error: Invalid input. Please provide valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
