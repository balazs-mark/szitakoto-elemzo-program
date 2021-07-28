#!/usr/bin/ python
# -*- coding: utf-8 -*-


from sys import argv as command_line_arguments
from modules.file_structure import FileStructure
from modules.analyze import Analyze
from modules.error import Error
from modules.fetch_data import FetchData
from modules.print_developer_and_program_version import print_developer_and_program_version
from modules.check_updates import CheckUpdate


class Run:

    def __init__(self):
        print_developer_and_program_version()
        CheckUpdate()
        FetchData()
        try:
            if command_line_arguments[1] == "--debug":
                FileStructure().print_more_details_for_debuging()
        except IndexError:
            pass
        Analyze().get_license_plates_in_all_events()
        Analyze().print_matches()
        Error().print_errors()


if __name__ == "__main__":
    Run()
