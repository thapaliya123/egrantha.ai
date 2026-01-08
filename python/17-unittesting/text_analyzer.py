"""
Unit testing example: text analysis
- TODO:
    - write a simple text-analysis function, which takes file name as its only parameters
    - Calculate: 
        - the number of lines in the file
        - the number of characters in the file
- Note: TDD (Test Driven Development) is a form of software development where tests are written 
first i.e. before you write the actual functionality to be tested.

Keypoints:
- The unittest module is a framework for developing reliable automated tests
- You define test cases by subclassing from unittest.TestCase
- The unittest.main() function is useful for running all of the tests in a module
- The setUp() and tearDown() fixtures are used to run code before and after each test method.
- Test methods are defined by creating method names that start with test_ on test case objects
- The various TestCase.assert... methods can be used to make a test method fail when the 
  right conditions aren't met
- Use TestCase.assertRaises() in a with statement to check that the right exceptions are thrown
"""

import os
import unittest
from typing import Tuple

def analyze_text(file_name: str) -> Tuple[int, int]:
    """
    Calculates the number of lines and characters in a file.
    """
    with open(file_name, 'r') as file_obj:
        file_content = file_obj.read()
        line_cnt = len(file_content.split("\n"))
        char_cnt = len(file_content)

    return line_cnt, char_cnt

class TextAnalysisTests(unittest.TestCase):
    """
    Test for the ``analyze_text()`` function
    """
    def setUp(self):
        """
        Fixture that creates a file for the text methods to use.
        """
        self.filename = "text_analysis_test_file.txt"
        with open(self.filename, 'w') as file_obj:
            file_obj.write("Hey\nI am learning python programming language")

    def test_function_runs(self):
        """
        Basic smoke test: does the function run.
        """
        analyze_text(self.filename)

    def test_line_count(self):
        """
        Check that the line count is correct
        """
        self.assertEqual(analyze_text(self.filename)[0], 2)

    def test_character_count(self):
        """
        Check that the character count is correct
        """
        self.assertEqual(analyze_text(self.filename)[1], 45)

    def test_no_such_file(self):
        """
        Check the proper exception is thrown for a missing file
        """
        with self.assertRaises(IOError):
            analyze_text('test')

    def test_no_deletion(self):
        """
        Check that the function doesn't delete the input file
        """
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def tearDown(self):
        """
        Fixture that deletes the files used by the test methods
        """
        try:
            os.remove(self.filename)
        except Exception:
            pass
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()

