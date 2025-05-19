#!/usr/bin/env python3

import sys
import argparse

def get_numbers_from_file(filepath):
    """Reads numbers from a file, one number per line."""
    numbers = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                # Optionally, handle or log lines that are not valid numbers
                print(f"Warning: Skipping invalid number in file: {line.strip()}", file=sys.stderr)
    return numbers

def get_numbers(args):
    # If a file is specified, read from it
    if args.file:
        return get_numbers_from_file(args.file)
    # If there are positional command line arguments, use those
    elif args.numbers:
        return [float(arg) for arg in args.numbers]
    
    # Otherwise, read from stdin (if no tty, or if explicitly no numbers/file given)
    # This part needs to be re-evaluated based on how argparse handles no args
    # For now, let's assume if no file and no numbers, it means stdin
    if not sys.stdin.isatty() or (not args.file and not args.numbers):
        try:
            print("Reading from stdin. Enter numbers separated by spaces, or one number per line, then Ctrl-D:", file=sys.stderr)
            input_lines = sys.stdin.read().strip()
            # Handle both space-separated and newline-separated numbers from stdin
            return [float(num) for num_group in input_lines.split('\n') for num in num_group.split() if num]
        except EOFError:
            return []
        except ValueError: # Catch error if stdin parsing fails
            print("Error: Invalid input from stdin. Please provide valid numbers.", file=sys.stderr)
            sys.exit(1) # Exit if stdin is used and is invalid
    return [] # Default to empty list if no input method yields numbers

def main():
    parser = argparse.ArgumentParser(description="Sort numbers provided via command line, file, or stdin.")
    parser.add_argument('numbers', nargs='*', help="Numbers to sort, provided directly as arguments.")
    parser.add_argument('-f', '--file', type=str, help="Path to a file containing numbers, one per line.")
    
    args = parser.parse_args()

    try:
        # Get numbers based on parsed arguments
        numbers = get_numbers(args)
        
        if not numbers:
            # Improved error message if no numbers are found from any source
            if args.file:
                print(f"Error: No valid numbers found in file: {args.file} or file is empty.", file=sys.stderr)
            elif args.numbers: # Should not happen if argparse requires numbers, but good for safety
                print("Error: No numbers provided as arguments.", file=sys.stderr)
            else: # No file, no direct args implies waiting for stdin or stdin was empty
                 print("Error: No numbers provided. Use arguments, a file with -f, or pipe input via stdin.", file=sys.stderr)
            sys.exit(1)
        
        # Sort the numbers
        sorted_numbers = sorted(numbers) # Default ascending sort
        
        # Print the sorted numbers
        print(" ".join(str(num) for num in sorted_numbers))
        
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except ValueError: # General catch-all for float conversion issues not caught earlier
        # This might be redundant if get_numbers handles all ValueErrors, but kept for safety.
        print(f"Error: Invalid input. Please ensure all inputs are valid numbers.", file=sys.stderr)
        sys.exit(1)
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
