import random
import unittest

from visualization.console.utils.console_constants import ConsoleConstants
from visualization.launcher.exceptions.bounds_exception import BoundsException
from visualization.launcher.exceptions.length_exception import LengthException
from visualization.launcher.launcher import Launcher
from visualization.launcher.utils.launcher_constants import LauncherConstants


class TestLauncher(unittest.TestCase):
    """unit tests for PyGame Console"""

    def setUp(self):
        """setUp is overridden and is needed for unit tests to run"""
        self.launcher = Launcher()


class TestInputVerification(TestLauncher):
    """unit tests for console input verification"""

    def test_is_response_yes(self):
        """asserts yes response is handled correctly"""
        # Given
        responseYes = "yes"
        responseYesAbbr = "y"
        responseNo = "no"
        responseNoAbbr = "n"

        # When
        isYes = self.launcher._Launcher__is_response_yes(responseYes)
        isYesAbbr = self.launcher._Launcher__is_response_yes(responseYesAbbr)
        isNotYes = self.launcher._Launcher__is_response_yes(responseNo)
        isNotYesAbbr = self.launcher._Launcher__is_response_yes(responseNoAbbr)

        # Then
        self.assertTrue(isYes)
        self.assertTrue(isYesAbbr)
        self.assertFalse(isNotYes)
        self.assertFalse(isNotYesAbbr)

    def test_is_response_no(self):
        """asserts no response is handled correctly"""
        # Given
        responseYes = "yes"
        responseYesAbbr = "y"
        responseNo = "no"
        responseNoAbbr = "n"

        # When
        isNo = self.launcher._Launcher__is_response_no(responseNo)
        isNoAbbr = self.launcher._Launcher__is_response_no(responseNoAbbr)
        isNotNo = self.launcher._Launcher__is_response_no(responseYes)
        isNotNoAbbr = self.launcher._Launcher__is_response_no(responseYesAbbr)

        # Then
        self.assertTrue(isNo)
        self.assertTrue(isNoAbbr)
        self.assertFalse(isNotNo)
        self.assertFalse(isNotNoAbbr)

    def test_decide_path(self):
        """asserts that given key words return correct file paths"""
        # Given
        file_name_not_given = "test_file_name"

        # When
        file_path_not_given = self.launcher._Launcher__decide_path(
            file_name_not_given)
        file_path_random_1 = self.launcher._Launcher__decide_path(
            LauncherConstants.FILE_CHOICE_RANDOM_1)
        file_path_random_2 = self.launcher._Launcher__decide_path(
            LauncherConstants.FILE_CHOICE_RANDOM_2)
        file_path_sorted = self.launcher._Launcher__decide_path(
            LauncherConstants.FILE_CHOICE_SORTED)
        file_path_reverse = self.launcher._Launcher__decide_path(
            LauncherConstants.FILE_CHOICE_REVERSE)

        # Then
        self.assertEqual(file_path_not_given, file_name_not_given)
        self.assertEqual(file_path_random_1, LauncherConstants.RANDOM_FILE_1_PATH)
        self.assertEqual(file_path_random_2, LauncherConstants.RANDOM_FILE_2_PATH)
        self.assertEqual(file_path_sorted, LauncherConstants.SORTED_FILE_PATH)
        self.assertEqual(file_path_reverse, LauncherConstants.REVERSED_FILE_PATH)

    def test_format_file_contents_out_of_limits(self):
        """asserts formatted content out of out-limits content is empty"""
        # Given
        contents = [str(ConsoleConstants.ELEMENT_UPPER_BOUND_LIMIT_EXCLUSIVE
                        )] * ConsoleConstants.MAX_LEN_ELEMENTS
        # When
        formatted = self.launcher._Launcher__format_file_contents(contents)

        # Then
        self.assertTrue(len(formatted) == 0)

    def test_format_file_contents_length_does_not_match(self):
        """asserts formatted content out of non-length matching content is
        empty"""
        # Given
        contents = [str(ConsoleConstants.ELEMENT_LOWER_BOUND_LIMIT_INCLUSIVE
                        )] * (ConsoleConstants.MAX_LEN_ELEMENTS +1)

        # When
        formatted = self.launcher._Launcher__format_file_contents(contents)

        # Then
        self.assertTrue(len(formatted) == 0)

    def test_format_file_contents_correct_format(self):
        """asserts formatted content out of correctly formatted content is
        returned properly"""
        # Given
        contents = [str(ConsoleConstants.ELEMENT_LOWER_BOUND_LIMIT_INCLUSIVE
                        )] * ConsoleConstants.MAX_LEN_ELEMENTS

        # When
        formatted = self.launcher._Launcher__format_file_contents(contents)

        # Then
        self.assertEqual([int(i) for i in contents], formatted)

    def test_verify_number_is_within_limits_correct(self):
        """asserts number within limits does not raise an exception"""
        # Given
        number = random.randrange(
                ConsoleConstants.ELEMENT_LOWER_BOUND_LIMIT_INCLUSIVE,
                ConsoleConstants.ELEMENT_UPPER_BOUND_LIMIT_EXCLUSIVE)

        # When
        self.launcher._Launcher__verify_number_is_within_limits(number)

        # Then
        self.assertTrue(True)

    def test_verify_number_is_within_limits_incorrect(self):
        """asserts number outside limits raises an exception"""
        # Given
        number = ConsoleConstants.ELEMENT_UPPER_BOUND_LIMIT_EXCLUSIVE + 1

        # Then
        with self.assertRaises(BoundsException):
            # When
            self.launcher._Launcher__verify_number_is_within_limits(number)

    def test_verify_length_correct(self):
        """asserts content with correct length does not raise an exception"""
        # Given
        numbers = [1] * ConsoleConstants.MAX_LEN_ELEMENTS
        no_numbers = []

        # When
        self.launcher._Launcher__verify_length(numbers)
        self.launcher._Launcher__verify_length(no_numbers)

        # Then
        self.assertTrue(True)

    def test_verify_length_incorrect(self):
        """asserts content with incorrect length raises an exception"""
        # Given
        numbers = [1] * (ConsoleConstants.MAX_LEN_ELEMENTS + 1)

        # Then
        with self.assertRaises(LengthException):
            # When
            self.launcher._Launcher__verify_length(numbers)














