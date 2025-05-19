import unittest
import subprocess
import os
import tempfile
import sys

# Path to the script to be tested
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'sort_numbers.py')

class TestNumberSorter(unittest.TestCase):

    def run_script(self, args, stdin_data=None):
        """Helper function to run the sort_numbers.py script."""
        command = [sys.executable, SCRIPT_PATH] + args
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=stdin_data)
        return stdout.strip(), stderr.strip(), process.returncode

    def test_cli_arguments(self):
        """Test sorting numbers passed as command-line arguments."""
        stdout, stderr, returncode = self.run_script(['5', '1', '4', '2', '3'])
        self.assertEqual(stdout, "1.0 2.0 3.0 4.0 5.0")
        self.assertEqual(stderr, "")
        self.assertEqual(returncode, 0)

    def test_cli_arguments_empty(self):
        """Test with no CLI arguments, should read from stdin (or show prompt)."""
        # This test is tricky because it expects stdin. 
        # We'll test stdin explicitly. If no args and no file, it prompts for stdin.
        # If stdin is also empty, it should error.
        stdout, stderr, returncode = self.run_script([], stdin_data="") # Empty stdin
        self.assertIn("Error: No numbers provided.", stderr)
        self.assertEqual(stdout, "")
        self.assertEqual(returncode, 1)

    def test_stdin_input(self):
        """Test sorting numbers passed via stdin."""
        stdout, stderr, returncode = self.run_script([], stdin_data="5 1 4 2 3\n")
        self.assertEqual(stdout, "1.0 2.0 3.0 4.0 5.0")
        self.assertIn("No file or direct arguments provided. Reading from stdin", stderr) # Expect prompt
        self.assertEqual(returncode, 0)

    def test_stdin_input_multiple_lines(self):
        """Test sorting numbers passed via stdin over multiple lines."""
        stdout, stderr, returncode = self.run_script([], stdin_data="5 1\n4 2\n3\n")
        self.assertEqual(stdout, "1.0 2.0 3.0 4.0 5.0")
        self.assertIn("No file or direct arguments provided. Reading from stdin", stderr)
        self.assertEqual(returncode, 0)
        
    def test_stdin_invalid_input(self):
        """Test invalid input via stdin."""
        stdout, stderr, returncode = self.run_script([], stdin_data="5 1 abc 2 3\n")
        self.assertIn("Error: Invalid input in stdin.", stderr)
        self.assertEqual(stdout, "")
        self.assertEqual(returncode, 1)

    def test_file_input(self):
        """Test sorting numbers from a file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_file.write("5\n1\n4.0\n2\n3.5\n")
            tmp_filepath = tmp_file.name
        
        try:
            stdout, stderr, returncode = self.run_script(['--file', tmp_filepath])
            self.assertEqual(stdout, "1.0 2.0 3.5 4.0 5.0")
            self.assertEqual(stderr, "")
            self.assertEqual(returncode, 0)
        finally:
            os.remove(tmp_filepath)

    def test_file_input_empty_lines_and_spaces(self):
        """Test sorting numbers from a file with empty lines and spaces."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_file.write("5\n  \n1\n\n4.0\n 2 \n3.5\n") # Includes an empty line and a line with just spaces
            tmp_filepath = tmp_file.name
        
        try:
            stdout, stderr, returncode = self.run_script(['--file', tmp_filepath])
            self.assertEqual(stdout, "1.0 2.0 3.5 4.0 5.0") # Sorted order
            self.assertEqual(stderr, "")
            self.assertEqual(returncode, 0)
        finally:
            os.remove(tmp_filepath)


    def test_empty_file_input(self):
        """Test with an empty file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_filepath = tmp_file.name
            # File is empty
        
        try:
            stdout, stderr, returncode = self.run_script(['--file', tmp_filepath])
            self.assertIn("Error: No numbers provided.", stderr)
            self.assertEqual(stdout, "")
            self.assertEqual(returncode, 1)
        finally:
            os.remove(tmp_filepath)

    def test_invalid_file_path(self):
        """Test behavior with a non-existent file."""
        non_existent_file = "non_existent_test_file.txt"
        stdout, stderr, returncode = self.run_script(['--file', non_existent_file])
        self.assertIn(f"Error: File not found: {non_existent_file}", stderr)
        self.assertEqual(stdout, "")
        self.assertEqual(returncode, 1)

    def test_invalid_file_content(self):
        """Test behavior with a file containing non-numeric data."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_file.write("5\n1\nabc\n2\n3\n")
            tmp_filepath = tmp_file.name
        
        try:
            stdout, stderr, returncode = self.run_script(['--file', tmp_filepath])
            self.assertIn(f"Error: File contains non-numeric data: {tmp_filepath}", stderr)
            self.assertEqual(stdout, "")
            self.assertEqual(returncode, 1)
        finally:
            os.remove(tmp_filepath)

    def test_cli_invalid_input(self):
        """Test invalid numeric input from CLI."""
        stdout, stderr, returncode = self.run_script(['5', '1', 'abc', '2', '3'])
        self.assertIn("usage: sort_numbers.py", stderr) # Argparse error
        self.assertIn("invalid float value: 'abc'", stderr) # Argparse error
        self.assertEqual(stdout, "")
        self.assertEqual(returncode, 2) # Argparse exits with 2 for bad args

    def test_priority_file_over_cli_args(self):
        """Test that file input is prioritized over CLI arguments if both are given (argparse default)."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_file.write("10\n20\n")
            tmp_filepath = tmp_file.name
        
        try:
            # The script logic explicitly prioritizes --file
            stdout, stderr, returncode = self.run_script(['--file', tmp_filepath, '1', '2', '3'])
            self.assertEqual(stdout, "10.0 20.0")
            self.assertEqual(stderr, "")
            self.assertEqual(returncode, 0)
        finally:
            os.remove(tmp_filepath)
            
    def test_cli_then_stdin_if_no_file(self):
        """Test that CLI args are used if present, and stdin is not prompted."""
        stdout, stderr, returncode = self.run_script(['30', '10'], stdin_data="1 2 3")
        self.assertEqual(stdout, "10.0 30.0")
        self.assertEqual(stderr, "") # No prompt for stdin
        self.assertEqual(returncode, 0)

if __name__ == '__main__':
    unittest.main() 