#!/usr/bin/ python
# -*- coding: utf-8 -*-


from .tabulator import Tabulator
from .events import events


class Analyze:
    license_plates_in_all_events = []

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
                for license_plate in self.license_plates_in_all_events:
                    print(f"{Tabulator.tab1}- {license_plate}")
            else:
                print(not_found_text)
        except TypeError:
            print(not_found_text)
        print("\n----------------------------------------------------------------------\n")
