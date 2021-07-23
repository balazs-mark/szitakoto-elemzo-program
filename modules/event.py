#!/usr/bin/ python
# -*- coding: utf-8 -*-


from .events import events


class Event:

    def __init__(self, name:str, license_plates:list):
        self.name = name
        self.license_plates = license_plates


    @classmethod
    def create_new_event_by_folder(cls, foldername):
        event_name = foldername.replace(" ", "_").lower()
        new_event = cls(name=event_name, license_plates=[])
        events.append(new_event)
