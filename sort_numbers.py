#!/usr/bin/env python3

import sys
import argparse

def get_numbers(args):
    # If a file is provided, read numbers from it
    if args.file:
        try:
            with open(args.file, 'r') as f:
                return [float(line.strip()) for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
        except ValueError:
            print(f"Error: Invalid content in file: {args.file}. Ensure each line contains a single number.")
            sys.exit(1)
    # If there are command line arguments (numbers directly), use those
    elif args.numbers:
        return [float(arg) for arg in args.numbers]
    
    # Otherwise, read from stdin
    try:
        input_line = sys.stdin.readline().strip()
        if not input_line:
            return []
        return [float(num) for num in input_line.split()]
    except EOFError:
        return []

def main():
    parser = argparse.ArgumentParser(description="Sort numbers from a file, command line arguments, or stdin.")
    parser.add_argument('numbers', nargs='*', help="Numbers to sort (if not using -f or stdin).")
    parser.add_argument('-f', '--file', help="Path to a file containing numbers, one per line.")
    
    args = parser.parse_args()

    try:
        # Get numbers based on parsed arguments
        numbers = get_numbers(args)
        
        if not numbers:
            print("Error: No numbers provided. Please provide numbers via file, arguments, or stdin.")
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
