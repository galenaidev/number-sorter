#!/usr/bin/env python3

import sys
import os
import argparse

def read_numbers_from_file(file_path):
    """Read numbers from a file, one number per line."""
    try:
        with open(file_path, 'r') as f:
            return [float(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        raise ValueError(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        raise ValueError(f"Error: Invalid number found in file '{file_path}'. Please ensure all lines contain valid numbers.")
    except Exception as e:
        raise ValueError(f"Error reading file '{file_path}': {str(e)}")

def get_numbers():
    parser = argparse.ArgumentParser(description='Sort numbers from command line arguments or a file.')
    parser.add_argument('numbers', nargs='*', type=float, help='Numbers to sort')
    parser.add_argument('-f', '--file', help='Input file containing one number per line')
    
    args = parser.parse_args()
    
    # If a file is specified, read numbers from it
    if args.file:
        return read_numbers_from_file(args.file)
    
    # If there are command line numbers, use those
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
        print(" ".join(str(num) for num in sorted_numbers))
        
    except ValueError as e:
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
