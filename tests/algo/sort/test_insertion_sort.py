import unittest

from algo.sort.insertion_sort import InsertionSortContainer
from visualization.console.utils.colors.sort_color_collection import \
    SortColorCollection


class TestInsertionSortContainer(unittest.TestCase):
    """unit tests for insertion sort container"""

    def setUp(self):
        """setUp is overridden and is needed for unit tests to run"""
        self.sort_container = InsertionSortContainer()


class TestSort(TestInsertionSortContainer):
    """unit tests for insertion sort container"""

    def test_sort(self):
        """asserts list is sorted"""
        # Given
        to_be_sorted = [2, 3, 1, 5, 4]
        color_collection = SortColorCollection()
        elements_in_colors = [color_collection.initial_bar_color] * len(to_be_sorted)

        # When
        self.sort_container.sort(to_be_sorted, elements_in_colors,
                                 color_collection, lambda *args: None)

        # Then
        self.assertEqual(to_be_sorted, [1, 2, 3, 4, 5])
