from algo.sort.sort_contract import SortContainerContract
from visualization.console.utils.colors.sort_color_collection import \
    SortColorCollection


class HeapSortContainer(SortContainerContract):
    """sort container for heap sort"""

    # overridden sort contract attributes
    name = "HEAP SORT"

    def sort(self, elements: list, elements_in_color: list,
             color_collection: SortColorCollection, console_update):
        """performs heap sort"""
        n = len(elements)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(elements, elements_in_color, color_collection,
                         console_update, i, n)
        for i in range(n - 1, 0, -1):
            elements[i], elements[0] = elements[0], elements[i]
            elements_in_color[i] = color_collection.finished_bar_color
            console_update()
            self.heapify(elements, elements_in_color, color_collection,
                         console_update, 0, i)

    def heapify(self, elements, elements_in_color: list, color_collection:
                SortColorCollection, console_update, root, size):
        """heapifies elements"""
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root
        if left < size and elements[left] > elements[largest]:
            largest = left
        if right < size and elements[right] > elements[largest]:
            largest = right
        if largest != root:
            elements_in_color[largest] = color_collection.sorting_bar_color
            elements_in_color[root] = color_collection.sorting_bar_color
            elements[largest], \
            elements[root] = elements[root], \
                             elements[largest]
            console_update()
            elements_in_color[largest] = color_collection.calculating_bar_color
            elements_in_color[root] = color_collection.calculating_bar_color
            self.heapify(elements, elements_in_color, color_collection,
                         console_update, largest,
                         size)
            console_update()
