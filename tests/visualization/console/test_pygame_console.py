import unittest

from visualization.console.pygame_console import PyGameConsole
from visualization.console.utils.console_constants import ConsoleConstants


class TestPyGameConsole(unittest.TestCase):
    """unit tests for PyGame Console"""

    def setUp(self):
        """setUp is overridden and is needed for unit tests to run"""
        pass


class TestInitialization(TestPyGameConsole):
    """unit tests for console initialization and methods for it"""

    def test_init(self):
        """asserts console is initialized properly"""
        # Given
        elements = [1] * ConsoleConstants.MAX_LEN_ELEMENTS

        # When
        console = PyGameConsole(elements)

        # Then
        self.assertEqual(console.elements, elements)

    def test_generate_random_elements(self):
        """asserts console is initialized with randomly generated elements"""
        # Given
        elements = []

        # When
        console = PyGameConsole(elements)

        # Then
        self.assertNotEqual(elements, console.elements)

    def test_set_elements(self):
        """asserts console is initialized with given elements"""
        # Given
        elements = [1] * ConsoleConstants.MAX_LEN_ELEMENTS

        # When
        console = PyGameConsole(elements)

        # Then
        self.assertEqual(elements, console.elements)


class TestRepresentation(TestPyGameConsole):
    """unit tests for console representation"""

    def test_repr(self):
        """asserts eval can be called"""
        # Given
        elements = [1] * ConsoleConstants.MAX_LEN_ELEMENTS
        console = PyGameConsole(elements)

        # When
        representation = console.__repr__()
        new_console = eval(representation)

        # Then
        self.assertTrue(isinstance(new_console, PyGameConsole))


class TestSetUp(TestPyGameConsole):
    """unit tests for console set up"""

    def test_set_up(self):
        """asserts set up is successful, makes sures there is no crash"""
        # Given
        elements = [1] * ConsoleConstants.MAX_LEN_ELEMENTS
        console = PyGameConsole(elements)

        # When
        console.set_up()

        # Then
        self.assertTrue(True)
