import time

from alarm.Alarm import Alarm

from analyzer.OdbParamAnalyzer import OdbParamAnalyzer
from analyzer.OdbSpeedAnalyzer import OdbSpeedAnalyzer
from analyzer.PostureAnalyzer import PostureAnalyzer


class EventProcessor(object):
    __processors = [PostureAnalyzer(), OdbSpeedAnalyzer(), OdbParamAnalyzer()]

    __alarm = Alarm()

    __num_exceptions_before_alarm = 2

    __dict = {}

    def __init__(self):
        for p in self.__processors:
            self.__dict.setdefault(p.__hash__(), [])
        print self.__dict

    def process(self):
        while True:
            print 'invoking analyzers'
            should_alarm = self.__should_alarm()
            print should_alarm
            if should_alarm:
                print 'alarming'
                self.__alarm.ring()
            time.sleep(5)

    def __should_alarm(self):
        for instance in self.__processors:
            print instance
            # maybe has the exception in the last 10-20 times?
            has_exception = instance.has_exception()
            # print dict[instance]
            self.__dict[instance.__hash__()].append(has_exception)
            print instance

            if len(self.__dict[instance.__hash__()]) >= self.__num_exceptions_before_alarm:
                return True
        return False



