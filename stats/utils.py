# -*- coding: utf-8 -*-
import smtplib
import traceback
from stats.config import FROM, TO, SERVER

__author__ = 'fearless'


class Logging(object):
    def __init__(self, subject, debug):
        if debug:
            print traceback.format_exc()
        else:
            self.send_mail(subject, traceback.format_exc())

    def send_mail(self, subject, content):
        message = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (FROM, ", ".join(TO), subject, content)

        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, message)
        server.quit()
