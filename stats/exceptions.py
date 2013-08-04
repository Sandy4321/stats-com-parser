__author__ = 'fearless'


class ParserNotExists(Exception):
    def __str__(self):
        return "Given parser type not implemented"


class FileWithPathNotExists(Exception):
    def __str__(self):
        return "Given filename with path not exists"
