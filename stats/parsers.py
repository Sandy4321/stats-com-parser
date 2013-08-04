# -*- coding: utf-8 -*-
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from stats.exceptions import ParserNotExists, FileWithPathNotExists
from stats.models import League, Division, Conference, Team
from stats.utils import Logging

__author__ = 'fearless'


class TeamHandler(ContentHandler):
    teams = []
    root = ['mlb','nba','nfl']
    season = ''
    league = None
    division = None
    conference = None
    team = None

    def startElement(self, name, attrs):
        if name in self.root:
            self.teams = []
        elif name == 'season':
            if attrs.get('year'):
                self.season = attrs.get('year')
            elif attrs.get('season'):
                self.season = attrs.get('season')
        elif name == 'league':
            self.league = League(attrs.get('id'), attrs.get('label'))
        elif name == 'conference':
            self.conference = Conference(attrs.get('id'), attrs.get('label'))
        elif name == 'division':
            self.division = Division(attrs.get('id'), attrs.get('label'))
        elif name == 'team':
            self.team = Team(id=attrs.get('id'), global_id=attrs.get('global-id'), name=attrs.get('name'), city=attrs.get('city'), alias=attrs.get('alias'), league=self.league, division=self.division, conference=self.conference, season=self.season)
        return

    def endElement(self, name):
        if name == 'team':
            self.teams.append(self.team)
        elif name in self.root:
            print self.teams
        return


class Parser(object):
    """
    filewithpath - is path to xml file

    parset_type - is type of parser, one of : team, roster

    debug - set this to 1 if you want display all errors, set it to 0, if you want send all error by email
    """
    def __init__(self, filewithpath, parser_type, debug=False):
        try:
            parser = make_parser()
            if parser_type == "team":
                currentHandler = TeamHandler()
            else:
                raise ParserNotExists()
            parser.setContentHandler(currentHandler)
            if os.path.exists(filewithpath):
                parser.parse(filewithpath)
            else:
                raise FileWithPathNotExists()
        except ParserNotExists:
            Logging(parser_type, debug)
        except FileWithPathNotExists:
            Logging(parser_type, debug)
