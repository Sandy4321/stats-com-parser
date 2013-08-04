#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from stats.parsers import Parser

__author__ = 'fearless'

if __name__ == "__main__":
    debug = False
    filewithpath = ''
    parser_type = ''
    if len(sys.argv) == 6:
        for i in range(1, 6):
            if sys.argv[i] == '-d':
                debug = True
            elif sys.argv[i] == '-t':
                parser_type = sys.argv[i+1]
            elif sys.argv[i] == '-f':
                filewithpath = sys.argv[i+1]

        Parser(filewithpath, parser_type, debug)
    else:
        print "-f <file_with_path> - You may specify XML files"
        print "-d for debug"
        print "-t <parser_type> for parser type one of team, roster"
        exit(0)
