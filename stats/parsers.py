# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from stats.exceptions import ParserNotExists
from stats.utils import Logging

__author__ = 'fearless'


class TeamHandler(ContentHandler):
    def __init__(self):
        self.id = 0

    def startElement(self, name, attrs):
        return

    def endElement(self, name):
        return


class Parser(object):
    def __init__(self, filewithpath, parser_type, debug):
        try:
            parser = make_parser()
            if parser_type == "team":
                currentHandler = TeamHandler()
            else:
                raise ParserNotExists()
            parser.setContentHandler(currentHandler)
            parser.parse(filewithpath)
        except ParserNotExists:
            Logging("Manager", debug)
            sys.exit(1)
