from os import path

from visualization.console.console_contract import ConsoleContract
from visualization.console.pygame_console import PyGameConsole
from visualization.console.utils.console_constants import ConsoleConstants
from visualization.launcher.exceptions.bounds_exception import BoundsException
from visualization.launcher.exceptions.length_exception import LengthException
from visualization.launcher.launcher_contract import LauncherContract
from visualization.launcher.utils.launcher_constants import LauncherConstants


class Launcher(LauncherContract):
    """implementation of LauncherContract. Class in charge of handling user
    input and validating it"""

    def launch(self):
        """implementation of launch"""
        self.__show_description()
        file_name = self.__request_input_file()
        formatted_content = self.__handle_file(file_name)
        self.__intialize_console(formatted_content)

    def __intialize_console(self, elements) -> ConsoleContract:
        """initializes and commences a console"""
        console = PyGameConsole(elements)
        console.set_up()
        console.start()

    def __show_description(self):
        """presents users with an initial description of the program"""
        print(LauncherConstants.PROJECT_DESCRIPTION)

    def __is_response_yes(self, response) -> bool:
        """checks is response is yes"""
        if response == LauncherConstants.YES_RESPONSE or response == \
                LauncherConstants.YES_RESPONSE_ABBR:
            return True
        return False

    def __is_response_no(self, response) -> bool:
        """checks is response is no"""
        if response == LauncherConstants.NO_RESPONSE or response == \
                LauncherConstants.NO_RESPONSE_ABBR:
            return True
        return False

    def __request_input_file(self) -> str:
        """prompts user a request for a custom file input"""
        file_entered = False
        while not file_entered:
            is_input_wanted = input(
                LauncherConstants.CUSTOM_FILE_INPUT_PROMPT).lower().strip()
            if self.__is_response_yes(is_input_wanted):
                return self.__on_file_input_wanted()
            elif self.__is_response_no(is_input_wanted):
                return ""
            else:
                file_entered = self.__on_invalid_input()

    def __on_file_input_wanted(self) -> str:
        """if file exists, then it returns file name to be opened"""
        file_name = ""
        file_not_found = True
        while file_not_found:
            file_name = input(LauncherConstants.FILE_PATH_PROMPT)
            file_name = self.__decide_path(file_name)
            file_not_found = not path.exists(file_name)
            if file_not_found:
                print(LauncherConstants.FILE_NOT_FOUND)
        return file_name

    def __decide_path(self, file_name) -> str:
        """checks if user entered a system given file"""
        file_name_upper = file_name.upper()
        if file_name_upper == LauncherConstants.FILE_CHOICE_RANDOM_1:
            path = LauncherConstants.RANDOM_FILE_1_PATH
        elif file_name_upper == LauncherConstants.FILE_CHOICE_RANDOM_2:
            path = LauncherConstants.RANDOM_FILE_2_PATH
        elif file_name_upper == LauncherConstants.FILE_CHOICE_SORTED:
            path = LauncherConstants.SORTED_FILE_PATH
        elif file_name_upper == LauncherConstants.FILE_CHOICE_REVERSE:
            path = LauncherConstants.REVERSED_FILE_PATH
        else:
            path = file_name
        return path

    def __on_invalid_input(self):
        """handles invalid input"""
        while True:
            should_repeat = input(LauncherConstants.INVALID_RESPONSE_PROMPT)\
                .lower().strip()
            if self.__is_response_yes(should_repeat):
                return False
            elif self.__is_response_no(should_repeat):
                return True

    def __handle_file(self, file_name) -> [int]:
        """handles file given"""
        if file_name == "":
            return []
        else:
            file = open(file_name)
            file_content = file.readlines()
            return self.__format_file_contents(file_content)

    def __format_file_contents(self, content: [str]) -> [int]:
        """checks for file contents and verifies validity"""
        formatted_content = []
        for line in content:
            line = line.strip('\n')
            split_content = line.split(',')
            for piece in split_content:
                try:
                    if piece != '':
                        piece = int(piece)
                        self.__verify_number_is_within_limits(piece)
                        formatted_content.append(piece)
                except ValueError:
                    print(LauncherConstants.NON_INT_EXCEPTION_ALERT)
                    return []
                except BoundsException:
                    print(LauncherConstants.BOUNDS_EXCEPTION_ALERT)
                    return []
        try:
            self.__verify_length(formatted_content)
            return formatted_content
        except LengthException:
            print(len(formatted_content))
            print(LauncherConstants.LENGTH_EXCEPTION_ALERT)
            return []

    def __verify_number_is_within_limits(self, number):
        """raises exception when a number is not within set bounds"""
        if number >= ConsoleConstants.ELEMENT_UPPER_BOUND_LIMIT_EXCLUSIVE:
            raise BoundsException
        elif number < ConsoleConstants.ELEMENT_LOWER_BOUND_LIMIT_INCLUSIVE:
            raise BoundsException

    def __verify_length(self, contents: [int]):
        """raises exception when contents are not of expected length"""
        if len(contents) == ConsoleConstants.MAX_LEN_ELEMENTS or len(
                contents) == 0:
            return
        raise LengthException
