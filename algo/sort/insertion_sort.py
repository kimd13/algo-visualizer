from algo.sort.sort_contract import SortContainerContract
from visualization.console.utils.colors.sort_color_collection import SortColorCollection


class InsertionSortContainer(SortContainerContract):
    """sort container for insertion sort"""

    # overridden sort contract attributes
    name = "INSERTION SORT"

    def sort(self, elements: list, elements_in_color: list,
             color_collection: SortColorCollection, console_update):
        """performs insertion sort"""
        for i in range(1, len(elements)):
            console_update()
            key = elements[i]
            elements_in_color[i] = color_collection.calculating_bar_color
            j = i - 1
            while j >= 0 and key < elements[j]:
                elements_in_color[j] = color_collection.sorting_bar_color
                elements[j + 1] = elements[j]
                console_update()
                elements_in_color[j] = color_collection.finished_bar_color
                j = j - 1
            elements[j + 1] = key
            console_update()
            elements_in_color[i] = color_collection.finished_bar_color
