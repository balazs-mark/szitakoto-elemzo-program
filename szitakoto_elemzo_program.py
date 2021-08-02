#!/usr/bin/ python
# -*- coding: utf-8 -*-


from config import Config
from sys import argv as command_line_arguments
from modules.file_structure import FileStructure
from modules.analyze import Analyze
from modules.error import Error
from modules.fetch_data import FetchData
from modules.print_developer_and_program_version import print_developer_and_program_version
from modules.check_updates import CheckUpdate
from modules.generate_txt import GenerateTXT
from modules.generate_html import GenerateHTML


class Run:

    def __init__(self):
        print_developer_and_program_version()
        CheckUpdate()
        FetchData()
        if "--debug" in command_line_arguments:
            FileStructure().print_more_details_for_debuging()
        Analyze().get_license_plates_in_all_events()
        GenerateTXT()
        GenerateHTML()
        Analyze().print_matches()
        Error().print_errors()


if __name__ == "__main__":
    Run()
