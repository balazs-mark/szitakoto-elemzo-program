#!/usr/bin/ python
# -*- coding: utf-8 -*-


import threading


class Config:
    data_source_folder = "tablazatok"
    version_in_use = "v1.4.0"

    name_of_results_txt_file = "talalatok.txt"
    name_of_results_html_file = "talalatok.html"

    would_print_into_txt = False
    would_print_into_html = False

    debug = False

    threading = True
