#!/usr/bin/ python
# -*- coding: utf-8 -*-


from modules.analyze import Analyze
from modules.error import Error
from modules.fetch_data import FetchData
from modules.print_developer_and_program_version import print_developer_and_program_version
from modules.check_updates import CheckUpdate
from modules.check_threading import CheckThreading
from modules.debug import Debug
from modules.generate_txt import GenerateTXT
from modules.generate_html import GenerateHTML


class Run:

    def __init__(self):
        Debug().check_debug_mode()
        CheckThreading().check_threading()
        print_developer_and_program_version()
        CheckUpdate()
        FetchData()
        Debug().print_debug_message()
        Analyze().get_license_plates_in_all_events()
        GenerateTXT()
        GenerateHTML()
        Analyze().print_matches()
        Error().print_errors()


if __name__ == "__main__":
    Run()
