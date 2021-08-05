#!/usr/bin/ python
# -*- coding: utf-8 -*-


try:
    import xlrd
except ImportError:
    from modules.error import HandleImportError
    HandleImportError()
import os
from sys import path
import threading
from .file_structure import FileStructure, file_structure
from .tabulator import Tabulator
from .event import Event
from .error import Error
from .events import events
from config import Config
from modules.license_plate import LicensePlate


class FetchData:

    all_license_plates = []


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
        threads = list()
        for foldername in folders_in_data_source_folder:
            full_path_to_folder = f"{path_of_folder_to_fetch}{foldername}/"
            FileStructure().add_folder(foldername)
            Event.create_new_event_by_folder(foldername)
            if Config.threading:
                new_thread = threading.Thread(target=self.get_xls_filenames_from_folder, args=(full_path_to_folder, event_number))
                threads.append(new_thread)
                new_thread.start()
                if Config.debug:
                    print(f"Thread-{event_number} started for {full_path_to_folder}")
            elif Config.threading == False:
                self.get_xls_filenames_from_folder(full_path_to_folder, event_number)
            event_number += 1
        if Config.threading:
            for full_path_to_folder, thread in enumerate(threads):
                thread.join()
                if Config.debug:
                    print(thread)
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


    def get_content_of_exel_file(self, path_to_exel_file, event_number):
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
                if license_plate_in_the_row != title_of_column:
                    self.add_license_plate_to_all_license_plates(license_plate_in_the_row, events[event_index_number].name)
                    if license_plate_in_the_row not in events[event_index_number].license_plates:
                        license_plates_in_sheet.append(license_plate_in_the_row)
            events[event_index_number].license_plates.extend(license_plates_in_sheet)
            sheet_index += 1


    def add_license_plate_to_all_license_plates(self, license_plate_number:str, name_of_containing_event:str):
        for item in self.all_license_plates:
            if item.license_plate_number == license_plate_number:
                item.names_of_containing_events.append(name_of_containing_event)
                return
        new_license_plate = LicensePlate(license_plate_number=license_plate_number, names_of_containing_events=[name_of_containing_event])
        self.all_license_plates.append(new_license_plate)
