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
            print("[ ] TXT fájl generálása...")
            self.generate_text_from_result()
            self.print_into_txt()
            print("[+] A TXT fájl elkészült.")


    def check_would_print_into_txt(self):
        try:
            if "--txt" in command_line_arguments:
                self.would_print_into_txt = True
        except IndexError:
            pass

    
    def generate_text_from_result(self):
        for license_plate in Analyze.license_plates_in_all_events:
            self.result_text = self.result_text + license_plate + "\n"
        self.result_text
    
    
    def print_into_txt(self):
        result_txt_file = open(Config.name_of_results_txt_file, "w")
        result_txt_file.write(self.result_text)
        result_txt_file.close()
