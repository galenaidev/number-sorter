#!/usr/bin/env python3

import sys
import os

def get_numbers():
    # If there are command line arguments, check if the first is a file
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        if os.path.isfile(first_arg):
            try:
                with open(first_arg, 'r') as f:
                    return [float(line.strip()) for line in f if line.strip()]
            except Exception as e:
                print(f"Error: Could not read file '{first_arg}': {e}")
                sys.exit(1)
        else:
            try:
                return [float(arg) for arg in sys.argv[1:]]
            except ValueError:
                print("Error: Invalid number in arguments.")
                sys.exit(1)
    
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
            print("Error: No numbers provided. Please provide numbers as arguments, a file, or through stdin.")
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
