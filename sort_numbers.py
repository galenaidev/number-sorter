#!/usr/bin/env python3

import sys

def get_numbers():
    # If there are command line arguments, use those
    if len(sys.argv) > 1:
        return [float(arg) for arg in sys.argv[1:]]
    
    # Otherwise, read from stdin
    try:
        input_line = sys.stdin.readline().strip()
        return [float(num) for num in input_line.split()]
    except EOFError:
        return []

def main():
    try:
        # Get numbers from either command line args or stdin
        numbers = get_numbers()
        
        if not numbers:
            print("Error: No numbers provided. Please provide numbers as arguments or through stdin.")
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
