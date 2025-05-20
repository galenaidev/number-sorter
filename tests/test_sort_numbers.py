import subprocess
import os
import sys

# Use sys.executable to ensure the same Python interpreter is used for the script
# This helps if pytest is run with `python3 -m pytest`
PYTHON_EXE = sys.executable
SCRIPT_NAME = "sort_numbers.py"

# Assuming tests are in 'number-sorter/tests/' and script is in 'number-sorter/'
# This path will be 'number-sorter/sort_numbers.py'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_PATH = os.path.join(PROJECT_ROOT, SCRIPT_NAME)


def run_script(args_list):
    """Helper function to run the sort_numbers.py script with arguments."""
    # Check if script exists at the determined path
    if not os.path.exists(SCRIPT_PATH):
        # This might happen if tests are run from a different working directory context.
        # Provide a more informative error.
        raise FileNotFoundError(
            f"Script {SCRIPT_NAME} not found at expected path: {SCRIPT_PATH}. "
            f"Ensure that sort_numbers.py is in the project root ({PROJECT_ROOT}) "
            f"and tests are run from the project root directory (e.g., 'number-sorter/')."
        )
        
    cmd = [PYTHON_EXE, SCRIPT_PATH] + [str(arg) for arg in args_list]
    # check=False to allow us to inspect returncode for failing commands.
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result

def test_sort_with_negative_numbers_from_issue():
    """Tests the specific case reported in GitHub issue #1."""
    input_numbers = [3, 1, -4, 1, 5, -9, 2, 6, -5, 3, 5]
    expected_output = "-9.0 -5.0 -4.0 1.0 1.0 2.0 3.0 3.0 5.0 5.0 6.0"
    
    result = run_script(input_numbers)
    
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output, (
        f"Output mismatch. Expected: '{expected_output}'. "
        f"Got: '{result.stdout.strip()}'"
    )

def test_sort_positive_integers():
    input_numbers = [5, 1, 4, 2, 8]
    expected_output = "1.0 2.0 4.0 5.0 8.0"
    result = run_script(input_numbers)
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output

def test_sort_with_floats():
    input_numbers = [3.14, 1.0, -2.71, 0.0]
    expected_output = "-2.71 0.0 1.0 3.14"
    result = run_script(input_numbers)
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output
    
def test_sort_already_sorted():
    input_numbers = [1, 2, 3, 4, 5]
    expected_output = "1.0 2.0 3.0 4.0 5.0"
    result = run_script(input_numbers)
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output

def test_sort_reverse_sorted():
    input_numbers = [5, 4, 3, 2, 1]
    expected_output = "1.0 2.0 3.0 4.0 5.0"
    result = run_script(input_numbers)
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output

def test_no_numbers_provided():
    result = run_script([])
    assert result.returncode == 1, (
        f"Expected return code 1 for no input, got {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert "Error: No numbers provided." in result.stdout.strip(), (
        f"Expected error message not found. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )

def test_invalid_input_non_numeric():
    input_numbers = [3, "a", 1]
    result = run_script(input_numbers)
    assert result.returncode == 1, (
        f"Expected return code 1 for invalid input, got {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert "Error: Invalid input. Please provide valid numbers." in result.stdout.strip(), (
        f"Expected error message not found for invalid input. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )

def test_single_number():
    input_numbers = [42]
    expected_output = "42.0"
    result = run_script(input_numbers)
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output

def test_duplicate_numbers():
    input_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] 
    expected_output = "1.0 1.0 2.0 3.0 3.0 4.0 5.0 5.0 5.0 6.0 9.0"
    result = run_script(input_numbers)
    assert result.returncode == 0, (
        f"Script exited with error code {result.returncode}. "
        f"Stdout: '{result.stdout.strip()}'. Stderr: '{result.stderr.strip()}'"
    )
    assert result.stdout.strip() == expected_output 