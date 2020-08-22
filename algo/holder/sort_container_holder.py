from algo.sort.insertion_sort import InsertionSortContainer
from algo.sort.heap_sort import HeapSortContainer
from algo.sort.sort_contract import SortContainerContract


class SortContainerHolder:
    """"holder for various sort containers"""

    __current_index = 0
    __holder = [HeapSortContainer(), InsertionSortContainer()]

    def get_current_container(self) -> SortContainerContract:
        """returns container at current index"""
        return self.__holder[self.__current_index]

    def shift_prev(self) -> SortContainerContract:
        """shift index to prev and returns container at that index"""
        if self.__current_index > 0:
            self.__current_index -= 1
        else:
            self.__current_index = len(self.__holder) - 1
        return self.get_current_container()

    def shift_forward(self) -> SortContainerContract:
        """shift index forward and returns container at that index"""
        if self.__current_index == len(self.__holder) - 1:
            self.__current_index = 0
        else:
            self.__current_index += 1
        return self.get_current_container()
