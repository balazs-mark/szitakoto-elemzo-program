#!/usr/bin/ python
# -*- coding: utf-8 -*-


from sys import argv as command_line_arguments

from config import Config


class CheckThreading:

    @staticmethod
    def check_threading():
        if "--no-threading" in command_line_arguments:
            Config.threading = False
