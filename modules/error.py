#!/usr/bin/ python
# -*- coding: utf-8 -*-


from .tabulator import Tabulator


class Error:
    files_could_not_read = []

    def print_errors(self):
        if len(self.files_could_not_read) != 0:
            print("\n\n\nA következő fájlok beolvasása nem sikerült:".upper())
            for could_not_read_filename in self.files_could_not_read:
                self.print_could_not_read_filename(could_not_read_filename)
                
    def print_could_not_read_filename(self, could_not_read_filename):
        print(f"{Tabulator.tab2}- {could_not_read_filename}")


class HandleImportError:

    def __init__(self):
        from modules.print_developer_and_program_version import print_developer_and_program_version
        print_developer_and_program_version()
        print("\n[-] HIBA: Hiányzó modul!")
        print("[!] Próbáld meg a 'pip install -r requirements.txt' parancs futtatását!\n")
        exit()
