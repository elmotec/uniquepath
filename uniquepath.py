#!/usr/bin/env python

"""Removes duplicates in a PATH-like environment variable."""

__version__ = '0.70'


import re
import os
import sys
import logging
from argparse import ArgumentParser


def is_word(val):
    """True if the argument is a string of characters only."""
    match = re.search('\W', val)
    return match is None


def normalize(pth):
    """Simply calls os.path.normpath for now."""
    norm_pth = os.path.normpath(pth)
    return norm_pth


class VariableManipulator(object):
    """Algortihms to manipulate environment variables."""
    def __init__(self, val, separator=None):
        self.separator = os.pathsep
        self.elements = []
        if separator:
            self.separator = separator
        if val:
            self.elements = [normalize(path)
                    for path in val.split(self.separator)]

    def get_value(self):
        """Converts path elements back to a string."""
        return self.separator.join(self.elements)

    def remove_duplicate_paths(self):
        """Removes duplicates in the variable value."""
        seen = set()
        filtered_elements = [
                el for el in self.elements
                if el.upper() not in seen and not seen.add(el.upper())]
        self.elements = filtered_elements

    def append_path(self, pth):
        """Appends pth at the end of the variable."""
        if not os.path.exists(pth):
            logging.warn("invalid path: {}".format(pth))
            return
        self.elements.append(pth)

    def prepend_path(self, pth):
        """Prepends pth at the begining of the variable."""
        if not os.path.exists(pth):
            raise RuntimeError("invalid pth")
        self.elements.insert(0, pth)

    def remove_path(self, pth):
        """Removes specific pth."""
        up_path = pth.upper()
        self.elements = [el for el in self.elements if el.upper() != up_path]


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    epilog = "On Windows: use {prog}.bat helper script.".format(prog=filename)
    parser = ArgumentParser(version=__version__, epilog=epilog)
    parser.add_argument("-r", "--remove", dest="remove",
            action="append", metavar="PATH",
            help="remove value(s) from the environment variable.")
    parser.add_argument("-a", "--append", dest="append",
            action="append", metavar="PATH",
            help="append value(s) to the environment variable.")
    parser.add_argument("-p", "--prepend", dest="prepend",
            action="append", metavar="PATH",
            help="prepend value(s) to the environment variable.")
    parser.add_argument("--separator", dest="sep", metavar="CHAR",
            help="changes the path separator (default is os specific).")
    parser.add_argument("--debug", action='store_true',
            help="different output format more readable but invalid. " +
            "DO NOT ASSIGN to an environment variable.")
    parser.add_argument("variable",
            help="environment variable or variable value to process.")
    arguments = parser.parse_args()
    variable_name = None
    value = arguments.variable  # Could be a variable name.
    if is_word(value):  # If so, converts it to the value.
        variable_name = value
        value = os.getenv(variable_name)
    manipulator = VariableManipulator(value, separator=arguments.sep)
    if arguments.remove:
        for path in arguments.remove:
            manipulator.remove_path(path)
    if arguments.append:
        for path in arguments.append:
            logging.info("adding {0} to {1}".format(path, manipulator))
            manipulator.append_path(path)
    if arguments.prepend:
        for path in arguments.prepend:
            logging.info("prepending {0} to {1}".format(path, manipulator))
            manipulator.prepend_path(path)
    manipulator.remove_duplicate_paths()
    value = manipulator.get_value()
    output = ""
    if arguments.debug:
        output = "\n".join(manipulator.elements)
    else:
        if sys.platform == 'win32':
            output = "set {0}={1}".format(variable_name, value)
        else:
            output = "{0}".format(manipulator.get_value())
    print(output)
