#!/usr/bin/ python
# -*- coding: utf-8 -*-


from .tabulator import Tabulator
from .events import events
from modules.fetch_data import FetchData


class Analyze:
    license_plates_in_all_events = []
    all_license_plates_ordered_by_often = []
    are_matches = False
    is_fetched_by_often = False


    def get_license_plates_in_all_events(self):
        print("[ ] Elemzés...")
        license_plates_of_first_event = events[0].license_plates
        for license_plate in license_plates_of_first_event:
            is_license_plate_in_all_event = True
            actualy_checking_event_index = 0
            while is_license_plate_in_all_event and actualy_checking_event_index < len(events):
                if license_plate in events[actualy_checking_event_index].license_plates:
                    actualy_checking_event_index += 1
                    is_license_plate_in_all_event = True
                else:
                    is_license_plate_in_all_event = False
            if is_license_plate_in_all_event:
                self.license_plates_in_all_events.append(license_plate)
        print("[+] Elemzés elkészült.")


    def print_matches(self):
        not_found_text = f"{Tabulator.tab2}Nincs olyan rendszám amelyik mindegyik eseménynél szerepel."
        print("\n\n----------------------------------------------------------------------")
        print(f"\nÖsszes eseményben szereplő rendszámok:\n")
        try:
            if len(self.license_plates_in_all_events) != 0:
                Analyze.are_matches = True
                for license_plate in self.license_plates_in_all_events:
                    print(f"{Tabulator.tab1}- {license_plate}")
            else:
                print(not_found_text)
        except TypeError:
            print(not_found_text)
        print("\n----------------------------------------------------------------------\n")


    def get_much_often_license_plates(self):
        answer = input("[?] Szeretnéd kilistázni a leggyakrabban előforduló rendszámokat? [ igen / NEM ]\n> ")
        print("")
        if answer.lower() == "igen" or answer.lower() == "i":
            Analyze.is_fetched_by_often = True
            self.print_license_plates_ordered_by_often()


    def reorder_all_license_plates_by_often(self):
        is_descending = True
        all_license_plates = FetchData.all_license_plates
        all_license_plates = sorted(all_license_plates, key=lambda license_plate: len(license_plate.names_of_containing_events), reverse=is_descending)
        return all_license_plates


    def print_license_plates_ordered_by_often(self):
        Analyze.all_license_plates_ordered_by_often = self.reorder_all_license_plates_by_often()
        for item in Analyze.all_license_plates_ordered_by_often:
            print(f"{item.license_plate_number} ({len(item.names_of_containing_events)} eseményben): {item.names_of_containing_events}")
