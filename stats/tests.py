import unittest
import sys
import cStringIO
from stats.exceptions import ParserNotExists, FileWithPathNotExists
from stats.parsers import Parser

__author__ = 'fearless'


class StatsTest(unittest.TestCase):
    def test_parser_create_object(self):
        Parser(parser_type="team", filewithpath="xmls/MLB_TEAM_INFO.XML",debug=True)

    def test_parser_return_error_message_if_parser_type_not_exists(self):
        parser = Parser(parser_type="team", filewithpath="xmls/MLB_TEAM_INFO.XML",debug=True)
        self.assertRaises(ParserNotExists, parser.__init__(parser_type="", filewithpath="MLB_TEAM_INFO.XML",debug=True))

    def test_parser_return_error_message_if_file_with_path_not_exists(self):
        parser = Parser(parser_type="team", filewithpath="xmls/MLB_TEAM_INFO.XML",debug=True)
        self.assertRaises(FileWithPathNotExists, parser.__init__(parser_type="team", filewithpath="MLB_TEAM_INFO.XML",debug=True))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        unittest.main()
    elif sys.argv[1] in ('-q','--quiet'):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(StatsTest))
        out = cStringIO.StringIO()
        results = unittest.TextTestRunner(stream=out).run(suite)
        if not results.wasSuccessful():
            for failure in results.failures:
                print "FAIL:", failure[0]
            for error in results.errors:
                print "ERROR:", error[0]
