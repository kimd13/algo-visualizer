class LauncherConstants:
    """keeps constants for launcher"""

    # Given path constants, from main.py
    RANDOM_FILE_1_PATH = "./visualization/launcher/assets/input_file_1"
    RANDOM_FILE_2_PATH = "./visualization/launcher/assets/input_file_2"
    SORTED_FILE_PATH = "./visualization/launcher/assets/input_file_3"
    REVERSED_FILE_PATH = "./visualization/launcher/assets/input_file_4"

    # Display constants
    PROJECT_DESCRIPTION = "This is ALGO VISUALIZER, with this program you " \
                          "will be able\nto view your algorithms in action " \
                          "and hopefully get a better\nsense of what's going " \
                          "on behind the scenes. "
    YES_RESPONSE = "yes"
    YES_RESPONSE_ABBR = "y"
    NO_RESPONSE = "no"
    NO_RESPONSE_ABBR = "n"
    CUSTOM_FILE_INPUT_PROMPT = "Enter Y/n if you wish to have a custom input " \
                               "file: "
    FILE_CHOICE_RANDOM_1 = "RANDOM_1"
    FILE_CHOICE_RANDOM_2 = "RANDOM_2"
    FILE_CHOICE_SORTED = "SORTED"
    FILE_CHOICE_REVERSE = "REVERSE SORTED"
    FILE_PATH_PROMPT = "Enter file path or type {} / {} " \
                       "/ {} / {}: ".format(FILE_CHOICE_RANDOM_1,
                                            FILE_CHOICE_RANDOM_2,
                                            FILE_CHOICE_SORTED,
                                            FILE_CHOICE_REVERSE)
    FILE_NOT_FOUND = "File not found."
    INVALID_RESPONSE_PROMPT = "Invalid response, would you like to try again " \
                              "[Y/n]? "
    NON_INT_EXCEPTION_ALERT = "Incorrect file contents. File contains non " \
                              "int values."
    BOUNDS_EXCEPTION_ALERT = "Incorrect file contents. File contains" \
                             " elements above/below bounds."
    LENGTH_EXCEPTION_ALERT = "Incorrect file contents. File does not contain " \
                             "required number of elements."
