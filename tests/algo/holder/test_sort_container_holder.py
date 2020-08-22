import unittest

from algo.holder.sort_container_holder import SortContainerHolder
from algo.sort.heap_sort import HeapSortContainer


class TestSortContainerHolder(unittest.TestCase):
    """unit tests for sort container holder"""

    def setUp(self):
        """setUp is overridden and is needed for unit tests to run"""
        self.sort_container_holder = SortContainerHolder()


class TestShift(TestSortContainerHolder):
    """tests shifting mechanism on sort container holder"""

    def test_get_current_container(self):
        """asserts default container is returned"""
        # Given
        default_container = HeapSortContainer()

        # When
        current_container = self.sort_container_holder.get_current_container()

        # Then
        self.assertEquals(type(current_container), type(default_container))

    def test_shift_prev(self):
        """asserts default container is not returned"""
        # Given
        default_container = HeapSortContainer()

        # When
        shift_prev_container = self.sort_container_holder.shift_prev()

        # Then
        self.assertNotEqual(type(default_container), type(shift_prev_container))


    def test_shift_forward(self):
        """asserts default container is not returned"""
        # Given
        default_container = HeapSortContainer()

        # When
        shift_forward_container = self.sort_container_holder.shift_forward()

        # Then
        self.assertNotEqual(type(default_container),
                            type(shift_forward_container))