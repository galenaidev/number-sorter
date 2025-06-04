#!/usr/bin/env python3
"""
Test script for sort_numbers.py
"""

import subprocess
import tempfile
import os
import sys

def run_command(cmd):
    """Run a command and return the output and exit code."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1

def test_command_line_args():
    """Test sorting with command-line arguments."""
    print("Testing command-line arguments...")
    stdout, stderr, code = run_command("python3 sort_numbers.py 5 2 8 1 9 3")
    expected = "1.0 2.0 3.0 5.0 8.0 9.0"
    assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
    assert code == 0, f"Expected exit code 0, got {code}"
    print("✓ Command-line arguments test passed")

def test_file_input():
    """Test sorting with file input."""
    print("Testing file input...")
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("5.5\n2\n8.1\n1\n9\n3.7\n\n7.2\n4\n")
        temp_file = f.name
    
    try:
        stdout, stderr, code = run_command(f"python3 sort_numbers.py --file {temp_file}")
        expected = "1.0 2.0 3.7 4.0 5.5 7.2 8.1 9.0"
        assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
        assert code == 0, f"Expected exit code 0, got {code}"
        print("✓ File input test passed")
    finally:
        os.unlink(temp_file)

def test_stdin_input():
    """Test sorting with stdin input."""
    print("Testing stdin input...")
    stdout, stderr, code = run_command("echo '5 2 8 1 9 3' | python3 sort_numbers.py")
    expected = "1.0 2.0 3.0 5.0 8.0 9.0"
    assert stdout == expected, f"Expected '{expected}', got '{stdout}'"
    assert code == 0, f"Expected exit code 0, got {code}"
    print("✓ Stdin input test passed")

def test_help():
    """Test help functionality."""
    print("Testing help...")
    stdout, stderr, code = run_command("python3 sort_numbers.py --help")
    assert "Sort numbers in ascending order" in stdout, "Help text should contain description"
    assert "--file" in stdout, "Help should mention --file option"
    assert code == 0, f"Expected exit code 0, got {code}"
    print("✓ Help test passed")

def test_file_not_found():
    """Test error handling for non-existent file."""
    print("Testing file not found error...")
    stdout, stderr, code = run_command("python3 sort_numbers.py --file nonexistent.txt")
    assert code != 0, "Should exit with non-zero code for missing file"
    print("✓ File not found error test passed")

def test_no_input():
    """Test error handling when no input is provided."""
    print("Testing no input error...")
    stdout, stderr, code = run_command("echo '' | python3 sort_numbers.py")
    assert code != 0, "Should exit with non-zero code when no numbers provided"
    print("✓ No input error test passed")

def main():
    """Run all tests."""
    print("Running tests for sort_numbers.py...\n")
    
    tests = [
        test_command_line_args,
        test_file_input,
        test_stdin_input,
        test_help,
        test_file_not_found,
        test_no_input
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
        print()
    
    print(f"Tests completed: {passed} passed, {failed} failed")
    
    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed! 🎉")

if __name__ == "__main__":
    main() 