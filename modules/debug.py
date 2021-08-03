#!/usr/bin/ python
# -*- coding: utf-8 -*-


from sys import argv as command_line_arguments

from config import Config
from modules.file_structure import FileStructure


class Debug:

    @staticmethod
    def print_debug_message():
        if Config.debug:
            FileStructure().print_more_details_for_debuging()


    @staticmethod
    def check_debug_mode():
        if "--debug" in command_line_arguments:
            Config.debug = True
