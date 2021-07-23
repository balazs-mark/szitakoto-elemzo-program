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
