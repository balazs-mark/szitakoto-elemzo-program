#!/usr/bin/ python
# -*- coding: utf-8 -*-


from config import Config
from modules.analyze import Analyze
from sys import argv as command_line_arguments


class GenerateHTML(Config):


    def __init__(self):
        self.result_html = ""
        self.check_would_print_into_html()
        if self.would_print_into_html:
            print("[ ] HTML fájl generálása...")
            self.generate_html_from_result()
            self.print_into_html()
            print("[+] A HTML fájl elkészült.")


    def check_would_print_into_html(self):
        if "--html" in command_line_arguments:
            self.would_print_into_html = True

    
    def generate_html_from_result(self):
        self.result_html = """
<!DOCTYPE html>
<html>
    <head>
    <title>Találatok | Szitakötő Elemző Program</title>
    </head>
    <body style="margin:3rem";>
        <h1 style="text-decoration: underline; font-weight: bold;">Találatok:</h1>
        <ul>\n"""
        for license_plate in Analyze.license_plates_in_all_events:
            self.result_html = self.result_html + f"\t\t\t<li>{license_plate}</li>\n"
        self.result_html = self.result_html + "\t\t</ul>\n\t</body>\n</html>"
    
    
    def print_into_html(self):
        result_html_file = open(Config.name_of_results_html_file, "w")
        result_html_file.write(self.result_html)
        result_html_file.close()
