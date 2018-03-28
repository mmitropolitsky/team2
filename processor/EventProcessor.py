import time

from alarm.Alarm import Alarm

from analyzer.OdbParamAnalyzer import OdbParamAnalyzer
from analyzer.OdbSpeedAnalyzer import OdbSpeedAnalyzer
from analyzer.PostureAnalyzer import PostureAnalyzer


class EventProcessor(object):
    __processors = [PostureAnalyzer(), OdbSpeedAnalyzer(), OdbParamAnalyzer()]

    __alarm = Alarm()

    __num_exceptions_before_alarm = 5

    __dict = {}

    def __init__(self):
        for p in self.__processors:
            self.__dict.setdefault(p, [True])
        print self.__dict

    def process(self):
        while True:
            print 'invoking analyzers'
            should_alarm = self.__should_alarm()
            print should_alarm
            if should_alarm:
                self.__alarm.ring()
            time.sleep(5)

    def __should_alarm(self):
        for instance in self.__processors:
            # maybe has the exception in the last 10-20 times?
            has_exception = instance.has_exception()
            if has_exception:
                self.__dict[instance].append(has_exception)
            print instance

            list_length = len(self.__dict[instance])

            print list_length
            mod = list_length % self.__num_exceptions_before_alarm
            bigger_than_threshold = list_length >= self.__num_exceptions_before_alarm
            print mod == 0 & bigger_than_threshold
            if mod == 0 & bigger_than_threshold:
                self.__dict[instance] = []
                print 'Alarm invoked by analyzer: ' + str(instance.__class__)
                return True

        return False
