from datetime import datetime
from django.conf import settings


class Utils(object):

    def get_logs(self):
        try:
            with open(settings.LOGFILE, 'r') as fd:
                data_logs = fd.readlines()
            return data_logs
        except IOError:
            return []

    def write_log(self, content):
        date = datetime.now()
        with open(settings.LOGFILE, 'a+') as fd:
            fd.write("%s  :  %s\n" % (date.strftime("%b %d %Y %H:%M:%S"), content))