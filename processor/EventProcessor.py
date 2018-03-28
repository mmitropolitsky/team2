import time

from analyzer.BaseAnalyzer import BaseAnalyzer
from analyzer.PostureAnalyzer import PostureAnalyzer


class EventProcessor(object):

    def process(self):
        while True:
            print 'invoking analyzers'
            print self.__should_alarm()
            self.__should_alarm()
            time.sleep(1)

    def __should_alarm(self):
        subclasses = BaseAnalyzer.__subclasses__()
        for cls in subclasses:
            print cls
            instance = cls()
            if instance.has_exception():
                return True
        return False



