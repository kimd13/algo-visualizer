import random
import pygame

from algo.holder.sort_container_holder import SortContainerHolder
from visualization.console.console_contract import ConsoleContract
from visualization.console.utils.colors.sort_color_collection import \
    SortColorCollection
from visualization.console.utils.colors.colors import Colors
from visualization.console.utils.console_constants import ConsoleConstants


class PyGameConsole(ConsoleContract):
    """implementation of console contract using pygame. Class in charge of
    handling visualization logic"""

    # overridden console attributes
    console_width = ConsoleConstants.CONSOLE_WIDTH
    console_height = ConsoleConstants.CONSOLE_HEIGHT
    elements = [0] * ConsoleConstants.MAX_LEN_ELEMENTS
    is_running = False
    sort_container_holder = SortContainerHolder()

    __title = ConsoleConstants.CONSOLE_TITLE

    # color related attributes
    __colors_collection = SortColorCollection()
    __elements_in_color = []

    # screen attributes
    __screen = None
    __screen_background_color = Colors.WHITE

    # font attributes
    __font_color = Colors.BLACK
    __font_style = ConsoleConstants.FONT_STYLE
    __font_size = ConsoleConstants.FONT_SIZE
    __font_style_large = None
    __font_style_small = None

    def __init__(self, elements: [int]):
        """constructor for console, initializes with given elements"""
        super().__init__(elements)
        self.current_sort_container = \
            self.sort_container_holder.get_current_container()  # defaults
        if elements:
            self.__set_elements(elements)
        else:
            self.__generate_random_elements()

    def __repr__(self):
        """representation of PyGameConsole"""
        return "PyGameConsole([])"

    def set_up(self) -> None:
        """sets up visualization before launch"""
        self.__init_screen()
        self.__init_font()
        self.__init_screen_titles()

    def start(self) -> None:
        """runs console, listening to user commands"""
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.__on_return_pressed()
                    elif event.key == pygame.K_BACKSPACE:
                        self.__on_backspace_pressed()
                    elif event.key == pygame.K_LEFT:
                        self.__on_left_pressed()
                    elif event.key == pygame.K_RIGHT:
                        self.__on_right_pressed()
            self.__draw()
            pygame.display.update()
        pygame.quit()

    def __on_return_pressed(self):
        """handles return pressed"""
        self.__set_elements_in_color()
        self.current_sort_container.sort(elements=
                                         self.elements,
                                         elements_in_color=
                                         self.__elements_in_color,
                                         color_collection=
                                         self.__colors_collection,
                                         console_update=
                                         self.__reload)

    def __on_backspace_pressed(self):
        """handles backspace pressed"""
        self.__generate_random_elements()
        self.__reload()

    def __on_left_pressed(self):
        """handles left pressed"""
        self.current_sort_container = self.sort_container_holder.shift_prev()
        self.__reload()

    def __on_right_pressed(self):
        """handles right pressed"""
        self.current_sort_container = self.sort_container_holder.shift_forward()
        self.__reload()

    def __reload(self):
        """reloads console to update visualization"""
        pygame.event.pump()
        self.__screen.fill(self.__screen_background_color)
        self.__init_screen_titles()
        self.__draw()
        pygame.display.update()
        pygame.time.delay(ConsoleConstants.TIME_DELAY)

    def __set_elements(self, elements: [int]):
        """sets elements in console"""
        self.elements = elements
        self.__set_elements_in_color()

    def __generate_random_elements(self):
        """generates elements in console"""
        self.__set_elements_in_color()
        for i in range(ConsoleConstants.MAX_LEN_ELEMENTS):
            self.elements[i] = random.randrange(
                ConsoleConstants.ELEMENT_LOWER_BOUND_LIMIT_INCLUSIVE,
                ConsoleConstants.ELEMENT_UPPER_BOUND_LIMIT_EXCLUSIVE)

    def __init_font(self) -> None:
        """initializes font"""
        pygame.font.init()
        self.__font_style_small = pygame.font.SysFont(self.__font_style,
                                                      self.__font_size)
        self.__font_style_large = pygame.font.SysFont(self.__font_style,
                                                      self.__font_size)

    def __init_screen_titles(self):
        """initializes screen titles"""
        pygame.display.set_caption(self.__title)
        self.__position_start_text()
        self.__position_generation_text()
        self.__position_algo_text()

    def __position_start_text(self):
        """positions start text"""
        start_text_position = (ConsoleConstants.VERTICAL_TEXT_POSITION,
                               ConsoleConstants.START_HORIZONTAL_POSITION)
        start_text = self.__font_style_large.render(ConsoleConstants.START_TEXT,
                                                    1,
                                                    self.__font_color)
        self.__screen.blit(start_text, start_text_position)

    def __position_generation_text(self):
        """positions backspace text for random generation"""
        generation_text_position = (ConsoleConstants.VERTICAL_TEXT_POSITION,
                                    ConsoleConstants.BACKSPACE_HORIZONTAL_POSITION)
        generation_text = self.__font_style_large.render \
            (ConsoleConstants.BACKSPACE_TEXT, 1, self.__font_color)
        self.__screen.blit(generation_text, generation_text_position)

    def __position_algo_text(self):
        """positions algorithm selection text"""
        algo_text_position = (ConsoleConstants.VERTICAL_TEXT_POSITION,
                              ConsoleConstants.ALGO_SELECTION_HORIZONTAL_POSITION)
        algo_text = self.__font_style_large.render(
            ConsoleConstants.ALGO_SELECTION_TEXT.format(
                self.current_sort_container.name), 1,
            self.__font_color)
        self.__screen.blit(algo_text, algo_text_position)

    def __init_screen(self):
        """initializes screen"""
        self.__screen = pygame.display.set_mode((self.console_width,
                                                 self.console_height))
        self.__screen.fill(self.__screen_background_color)

    def __draw(self):
        """draws console elements"""
        element_width = (self.console_width - ConsoleConstants.MAX_LEN_ELEMENTS) \
                        // ConsoleConstants.MAX_LEN_ELEMENTS
        self.__draw_lines(element_width)

    def __draw_lines(self, element_width: int):
        """draws line representations of elements"""
        for i in range(ConsoleConstants.MAX_LEN_ELEMENTS):
            pygame.draw.line(self.__screen, self.__elements_in_color[i],
                             self.__calculate_start_pos(i),
                             self.__calculate_end_pos(i),
                             element_width)

    def __calculate_start_pos(self, range_idx: int) -> tuple:
        """returns vector (x, y) of start position"""
        x = (900 / 150) * range_idx - 3
        y = 100
        return x, y

    def __calculate_end_pos(self, range_idx: int) -> tuple:
        """returns vector (x, y) of end position"""
        x = (900 / 150) * range_idx - 3
        y = self.elements[range_idx] * (
                550 / 100) + 100
        return x, y

    def __set_elements_in_color(self):
        """sets elements in color"""
        self.__elements_in_color = \
            [self.__colors_collection.initial_bar_color] \
            * ConsoleConstants.MAX_LEN_ELEMENTS
