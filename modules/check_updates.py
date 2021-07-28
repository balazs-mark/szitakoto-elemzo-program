#!/usr/bin/ python
# -*- coding: utf-8 -*-

try:
    import requests
except ImportError:
    print("\n[-] Hiba: Hiányzó modul!")
    print("[!] Próbáld meg a 'pip install -r requirements.txt' parancs futtatását!\n")
from config import Config


class CheckUpdate:

    version_in_use = Config.version_in_use

    username_of_developer = "balazs-mark"
    name_of_project = "szitakoto-elemzo-program"

    def __init__(self):
        self.latest_release_version = self.get_latest_release_number()
        self.print_result()

    def get_latest_release_number(self):
        self.url_of_latest_release = f"https://github.com/{self.username_of_developer}/{self.name_of_project}/releases/latest"
        response = requests.get(self.url_of_latest_release)
        redirected_url = response.url
        latest_release_version = redirected_url.split("/")[-1]
        return latest_release_version

    def print_result(self):
        if self.version_in_use == self.latest_release_version:
            print("[+] A program naprakész.")
        else:
            print("[!] A program új verziója elérhető!")
            print(f"    A letöltéshez látogass el a {self.url_of_latest_release} oldalra.")


if __name__ == "__main__":
    CheckUpdate()
