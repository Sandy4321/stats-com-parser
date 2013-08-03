# -*- coding: utf-8 -*-
__author__ = 'fearless'


class Update(object):
    datetime = ''
    version = 0

    def __init__(self, datetime, version):
        self.datetime = datetime
        self.version = version

    def __repr__(self):
        return "<Update %s object>" % self.datetime

    def save(self):
        return True


class League(object):
    id = 0
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<League %s object>" % self.name

    def save(self):
        return True


class Division(object):
    id = 0
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Division %s object>" % self.name

    def save(self):
        return True


class Team(object):
    league = None
    season = ''
    division = None
    id = 0
    global_id = 0
    city = ''
    name = ''
    alias = ''

    def __init__(self, league, division, season, id, global_id, name, city, alias):
        self.league = league
        self.division = division
        self.season = season
        self.id = id
        self.global_id = global_id
        self.name = name
        self.city = city
        self.alias = alias

    def __repr__(self):
        return "<Team %s object>" % self.name

    def save(self):
        return True
