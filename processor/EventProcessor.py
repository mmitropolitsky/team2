import time

from alarm.Alarm import Alarm
from analyzer.BaseAnalyzer import BaseAnalyzer
from analyzer.PostureAnalyzer import PostureAnalyzer


class EventProcessor(object):

    __alarm = Alarm()

    def process(self):
        while True:
            print 'invoking analyzers'
            print self.__should_alarm()
            if self.__should_alarm():
                print 'alarming'
                self.__alarm.ring()
            time.sleep(1)

    def __should_alarm(self):
        subclasses = BaseAnalyzer.__subclasses__()
        for cls in subclasses:
            instance = cls()
            # maybe has the exception in the last 10-20 times?
            if instance.has_exception():
                return True
        return False



