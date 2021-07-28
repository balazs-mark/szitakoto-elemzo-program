#!/usr/bin/ python
# -*- coding: utf-8 -*-


try:
    import xlrd
except ImportError:
    from modules.error import HandleImportError
    HandleImportError()
import os
from .file_structure import FileStructure, file_structure
from .tabulator import Tabulator
from .event import Event
from .error import Error
from .events import events
from config import Config


class FetchData:

    def __init__(self):
        self.fetch_data_from_data_source_folder()


    def fetch_data_from_data_source_folder(self):
        data_source_folder = Config.data_source_folder
        event_number = 1
        print("\n\n[ ] Fájlok olvasása...")
        current_directory_path = str(os.getcwd())
        path_of_folder_to_fetch = f"{current_directory_path}\\{data_source_folder}\\"
        file_structure.append(f"\nRead files:")
        try:
            folders_in_data_source_folder = os.listdir(path_of_folder_to_fetch)
        except FileNotFoundError:
            print(f"\n[-] HIBA: Nem található fájl a '{data_source_folder}' mappában.")
            print("[!] Kérlek ellenőrizd, hogy megfelelő módon elhelyezted-e az Exel fájlokat!\n")
            exit()
        for foldername in folders_in_data_source_folder:
            full_path_to_folder = f"{path_of_folder_to_fetch}{foldername}/"
            FileStructure().add_folder(foldername)
            Event.create_new_event_by_folder(foldername)
            self.get_xls_filenames_from_folder(full_path_to_folder, event_number)
            event_number += 1
        if len(file_structure) == 1:
            print(f"\n[-] HIBA: Nem olvashatóak adatok a '{data_source_folder}' mappából.".upper())
            print("[!] Kérlek ellenőrizd, hogy megfelelő módon elhelyezted-e az Exel fájlokat!\n")
            exit()
        print("[+] Fájlok beolvasva.")


    def get_xls_filenames_from_folder(self, full_path_to_folder, event_number):
        filenames_in_folder = os.listdir(full_path_to_folder)
        if len(filenames_in_folder) != 0:
            for filename in filenames_in_folder:
                if ".xls" in filename:
                    full_path_to_file = f"{full_path_to_folder}/{filename}"
                    FileStructure().add_filename(filename)
                    try:            
                        self.get_content_of_exel_file(full_path_to_file, event_number)
                    except:
                        Error().files_could_not_read.append(f"{full_path_to_folder}/{filename}")
                else:
                    Error().files_could_not_read.append(f"{full_path_to_folder}/{filename}")


    @staticmethod
    def get_content_of_exel_file(path_to_exel_file, event_number):
        exel_file_content = xlrd.open_workbook(path_to_exel_file)
        number_of_sheets = 0
        for sheet_name in exel_file_content.sheet_names():
            FileStructure().add_sheetname(sheet_name)
            number_of_sheets += 1
        sheet_index = 0
        while sheet_index < number_of_sheets:
            sheet_content = exel_file_content.sheet_by_index(sheet_index)
            license_plates_in_sheet = []
            event_index_number = event_number - 1
            for row_number in range(sheet_content.nrows):
                column_of_license_plate = 3
                title_of_column = "rendszám"
                license_plate_in_the_row = sheet_content.cell_value(rowx=row_number, colx=column_of_license_plate)
                if license_plate_in_the_row not in events[event_index_number].license_plates:
                    license_plates_in_sheet.append(license_plate_in_the_row)
            license_plates_in_sheet.remove(title_of_column)
            events[event_index_number].license_plates.extend(license_plates_in_sheet)
            sheet_index += 1
