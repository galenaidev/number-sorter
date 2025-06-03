#!/usr/bin/env python3

import sys
import argparse
import os

def read_numbers_from_file(filepath):
    """Read numbers from a file, one per line."""
    numbers = []
    try:
        with open(filepath, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"Error: Invalid number '{line}' on line {line_num} in file '{filepath}'")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}")
        sys.exit(1)
    
    return numbers

def get_numbers():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Sort numbers from command line arguments, file, or stdin')
    parser.add_argument('-f', '--file', help='File containing numbers to sort (one per line)')
    parser.add_argument('numbers', nargs='*', type=float, help='Numbers to sort')
    
    args = parser.parse_args()
    
    # If file is specified, read from file
    if args.file:
        return read_numbers_from_file(args.file)
    
    # If there are command line number arguments, use those
    if args.numbers:
        return args.numbers
    
    # Otherwise, read from stdin
    try:
        input_line = sys.stdin.readline().strip()
        return [float(num) for num in input_line.split()]
    except EOFError:
        return []

def main():
    try:
        # Get numbers from either command line args, file, or stdin
        numbers = get_numbers()
        
        if not numbers:
            print("Error: No numbers provided. Please provide numbers as arguments, through a file (-f), or through stdin.")
            sys.exit(1)
        
        # Sort the numbers
        sorted_numbers = sorted(numbers)
        
        # Print the sorted numbers
        formatted_numbers = []
        for num in sorted_numbers:
            if num == int(num):
                formatted_numbers.append(str(int(num)))
            else:
                formatted_numbers.append(str(num))
        print(" ".join(formatted_numbers))
        
    except ValueError as e:
        print(f"Error: Invalid input. Please provide valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
