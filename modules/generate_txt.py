#!/usr/bin/ python
# -*- coding: utf-8 -*-


from config import Config
from modules.analyze import Analyze
from sys import argv as command_line_arguments


class GenerateTXT(Config):


    def __init__(self):
        self.result_text = ""
        self.check_would_print_into_txt()
        if self.would_print_into_txt:
            print("\n[ ] TXT fájl generálása...")
            self.generate_text_from_result()
            self.print_into_txt()
            print("[+] A TXT fájl elkészült.")


    def check_would_print_into_txt(self):
        if "--txt" in command_line_arguments:
            self.would_print_into_txt = True

    
    def generate_text_from_result(self):
        if Analyze.are_matches:
            for license_plate in Analyze.license_plates_in_all_events:
                self.result_text = self.result_text + license_plate + "\n"
        elif Analyze.are_matches == False and Analyze.is_fetched_by_often:
            for item in Analyze.all_license_plates_ordered_by_often:
                self.result_text = self.result_text + f"{item.license_plate_number} ({len(item.names_of_containing_events)} eseményben): {item.names_of_containing_events}\n"
        else:
            self.result_text
    
    
    def print_into_txt(self):
        result_txt_file = open(Config.name_of_results_txt_file, "w")
        result_txt_file.write(self.result_text)
        result_txt_file.close()
