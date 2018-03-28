import time

import sqlite3

from alarm.Alarm import Alarm

from analyzer.PostureAnalyzer import PostureAnalyzer
from analyzer.ObdParamsAnalyzer import ObdParamsAnalyzer



class EventProcessor(object):
    #__processors = [PostureAnalyzer(), ObdParamsAnalyzer()]
    __processors = [ObdParamsAnalyzer()]

    __alarm = Alarm()

    __num_exceptions_before_alarm = 2

    __dict = {}

    def __init__(self):
        for p in self.__processors:
            self.__dict.setdefault(p.__hash__(), [])
        print self.__dict

    def process(self):
        i = 0
        while i<15:
            print 'invoking analyzers'
            should_alarm = self.__should_alarm()
            print should_alarm
            if should_alarm:
                print 'alarming'
                self.__alarm.ring()
            time.sleep(5)
            i+=1
        self.__finaly()

    def __finaly(self):
        for instance in self.__processors:
            instance.finalize()

    def __should_alarm(self):
        for instance in self.__processors:
            # maybe has the exception in the last 10-20 times?
            has_exception = instance.has_exception()
            # print dict[instance]
            self.__dict[instance.__hash__()].append(has_exception)
            if len(self.__dict[instance.__hash__()]) >= self.__num_exceptions_before_alarm:
                return True
        return False



