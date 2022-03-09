#!/usr/bin/ python
# -*- coding: utf-8 -*-


from config import Config


def print_developer_and_program_version():
    print(f"""
 ______________________________________________________________________________________________________
|                                                                                                      |
|     Szitakötő Elemző Program ({Config.version_in_use})                                                                |
|     Legfrisebb verzió letöltése: https://github.com/balazs-mark/szitakoto-elemzo-program             |
|______________________________________________________________________________________________________|
|                                                                                                      |
|     Hiba vagy további képesség kérése esetén kérlek vedd fel a kapcsolatot a fejlesztővel:           |
|                                                                                                      |
|         Márk Balázs r. hdgy.                                                                         |
|         BRFK BÜFO KBEO                                                                               |
|         06-20/563-10-12                                                                              |
|         markb@budapest.police.hu                                                                     |
|______________________________________________________________________________________________________|
""")
