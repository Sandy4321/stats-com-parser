#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from stats.parsers import Parser
from stats.utils import Logging

__author__ = 'fearless'

if __name__ == "__main__":
    debug = 1
    try:
        debug = int(sys.argv[1] or 0)
        parser_type = sys.argv[2]
        filewithpath = sys.argv[3]
        Parser(filewithpath, parser_type, debug)
    except IndexError:
        Logging("Manager", debug)
        sys.exit(1)
