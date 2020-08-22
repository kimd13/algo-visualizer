class ConsoleContract:
    """contract for set of operations to be overridden to be considered a
    Console"""

    is_running = None

    console_width = None
    console_height = None

    elements = None
    current_sort_container = None
    sort_container_holder = None

    def __init__(self, elements: [int]):
        """initializes console with elements to be visualized"""
        pass

    def __repr__(self):
        """returns pretty representation of console"""
        pass

    def set_up(self) -> None:
        """sets up console before start up"""
        pass

    def start(self) -> None:
        """starts console"""
        pass
