import pytest
from part1.main import get_calibration_value, parse_input_file
from io import StringIO
import sys

# Define a fixture for the input file simulation
@pytest.fixture
def input_file_digits(tmp_path):
    # Simulate an input file for digits
    input_file = tmp_path / "day1_advent_of_code.txt"
    input_file.write_text("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet")
    return input_file


@pytest.fixture
def input_file_words(tmp_path):
    # Simulate an input file for words
    input_file = tmp_path / "day1_advent_of_code.txt"
    input_file.write_text("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen")
    return input_file


def test_get_calibration_value():
    # Test cases with digits only
    assert get_calibration_value("1abc2") == 12
    assert get_calibration_value("pqr3stu8vwx") == 38
    assert get_calibration_value("a1b2c3d4e5f") == 15
    assert get_calibration_value("treb7uchet") == 77

    # Test cases with words, assuming expected behavior
    # Since get_calibration_value is not designed to handle words, it should raise an error or fail these cases.
    with pytest.raises(IndexError):
        get_calibration_value("two1nine")
    with pytest.raises(IndexError):
        get_calibration_value("eightwothree")


def test_parse_input_file(input_file_digits):
    # Test parsing input file with digits only
    global INPUT_FILE_PATH
    INPUT_FILE_PATH = str(input_file_digits)  # Redefine to use test fixture
    lines = parse_input_file()
    assert lines == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_main_output(input_file_digits, capsys):
    # Test the main function with digits only
    global INPUT_FILE_PATH
    INPUT_FILE_PATH = str(input_file_digits)
    from part1.main import main
    main()
    captured = capsys.readouterr()
    assert "142\n" in captured.out


def test_second_implementation_output(input_file_digits, capsys):
    # Capture stdout for the second implementation
    sys.stdin = StringIO("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet")
    from adventofcode.day1_2023 import part2
    part2.main()
    captured = capsys.readouterr()
    assert "142\n" in captured.out

    # Repeat test for words input
    sys.stdin = StringIO("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen")
    part2.main()
    captured = capsys.readouterr()
    assert "93\n" in captured.out

def test_second_implementation_handles_words_correctly(capsys):
    # Test case for second implementation with word inputs
    sys.stdin = StringIO("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen")
    from adventofcode.day1_2023.part2 import main
    main()
    captured = capsys.readouterr()
    assert captured.out == "93\n"