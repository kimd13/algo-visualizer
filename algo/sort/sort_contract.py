from visualization.console.utils.colors.sort_color_collection import SortColorCollection


class SortContainerContract:
    """contract for set of operations to be overridden to be considered a
        Sorting Container"""

    name = None

    def sort(self, elements: list, elements_in_color: list,
             color_collection: SortColorCollection, console_update):
        """perform sorting algorithm given elements, those elements
        represented in colors, a collection of colors for representing the
        state of sorting, and an updating function for visualization refreshing"""
        pass
