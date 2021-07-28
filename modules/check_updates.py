#!/usr/bin/ python
# -*- coding: utf-8 -*-

from config import Config
try:
    import requests
except ImportError:
    from modules.error import HandleImportError
    HandleImportError()


class CheckUpdate:

    version_in_use = Config.version_in_use

    username_of_developer = "balazs-mark"
    name_of_project = "szitakoto-elemzo-program"

    def __init__(self):
        print()
        print("[ ] Frissítés keresése...")
        try:
            self.latest_release_version = self.get_latest_release_number()
            self.print_result()
        except:
            print("\n[-] HIBA: A program verziójának frissessége hálózati hiba miatt nem ellenőrizhető. (valószínűleg a céges tűzfal blokkolja a frissítést)")
            print(f"    A legfrisebb verziót a {self.url_of_latest_release} oldalon eléred.")


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
