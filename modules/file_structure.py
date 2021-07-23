#!/usr/bin/ python
# -*- coding: utf-8 -*-


from .tabulator import Tabulator
from .events import events

file_structure = []

class FileStructure:

    def add_folder(self, foldername):
        file_structure.append(f"{Tabulator.tab2}- {foldername} (mappa)")
    
    def add_filename(self, filename):
        file_structure.append(f"{Tabulator.tab3}- {filename} (Exel fájl)")

    def add_sheetname(self, sheet_name):
        file_structure.append(f"{Tabulator.tab4}- {sheet_name} (fül)")

    def print_file_structure(self):
        for item in file_structure:
            print(item)

    def print_more_details_for_debuging(self):
        print("\n\n-------------------------  DEBUGING  -------------------------")
        self.print_file_structure()
        print()
        for event in events:
            print(f"Event name:'{event.name}'")
            print(f"License plates: {event.license_plates}")
            print()
        print("------------------------  END OF DEBUGING  ------------------------\n\n")
