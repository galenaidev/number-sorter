#!/usr/bin/env python3

import subprocess
import sys
import os
import tempfile

def run_command(cmd):
    """Run a command and return stdout, stderr, and return code."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_command_line_args():
    """Test command line argument functionality."""
    print("Testing command line arguments...")
    stdout, stderr, returncode = run_command("python3 sort_numbers.py 5 2 8 1 9 3")
    expected = "1 2 3 5 8 9"
    assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
    assert returncode == 0, f"Expected return code 0, got {returncode}"
    print("✓ Command line arguments test passed")

def test_file_input():
    """Test file input functionality."""
    print("Testing file input...")
    stdout, stderr, returncode = run_command("python3 sort_numbers.py -f test_numbers.txt")
    expected = "-5 -1.5 0 2.718 3.14 7 15 42 99 100"
    assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
    assert returncode == 0, f"Expected return code 0, got {returncode}"
    print("✓ File input test passed")

def test_stdin_input():
    """Test stdin input functionality."""
    print("Testing stdin input...")
    stdout, stderr, returncode = run_command("echo '5 2 8 1 9 3' | python3 sort_numbers.py")
    expected = "1 2 3 5 8 9"
    assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
    assert returncode == 0, f"Expected return code 0, got {returncode}"
    print("✓ Stdin input test passed")

def test_help():
    """Test help functionality."""
    print("Testing help functionality...")
    stdout, stderr, returncode = run_command("python3 sort_numbers.py -h")
    assert "Sort numbers" in stdout, f"Help text should contain 'Sort numbers', got '{stdout}'"
    assert returncode == 0, f"Expected return code 0, got {returncode}"
    print("✓ Help test passed")

def test_file_not_found():
    """Test error handling for non-existent file."""
    print("Testing file not found error...")
    stdout, stderr, returncode = run_command("python3 sort_numbers.py -f nonexistent.txt")
    assert returncode != 0, f"Expected non-zero return code for missing file"
    print("✓ File not found error test passed")

def test_empty_input():
    """Test error handling for empty input."""
    print("Testing empty input error...")
    stdout, stderr, returncode = run_command("echo '' | python3 sort_numbers.py")
    assert returncode != 0, f"Expected non-zero return code for empty input"
    print("✓ Empty input error test passed")

def main():
    """Run all tests."""
    print("Running functionality tests for number sorter...\n")
    
    try:
        test_command_line_args()
        test_file_input()
        test_stdin_input()
        test_help()
        test_file_not_found()
        test_empty_input()
        
        print("\n🎉 All tests passed!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 