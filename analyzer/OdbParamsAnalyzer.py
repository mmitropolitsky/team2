from analyzer.BaseAnalyzer import BaseAnalyzer
from adapter.ObdAdapter import ObdAdapter


class OdbParamsAnalyzer(BaseAnalyzer):

    def __init__(self):
        self.__adapter = ObdAdapter()
        self.__log_entries = []
        self.__slopes = dict()
        self.__log_entry = None

    def has_exception(self):
        return not self.__is_typical()

    def __is_typical(self):
        self.__log_entry, slope = self.__adapter.get_log_entry_and_slopes(self.__log_entry)
        self.__log_entries.append(self.__log_entry)
        self.__add_slope(slope)
        print self.__slopes
        return True

    def __add_slope(self, slope):
        for key in slope:
            if not key in self.__slopes:
                self.__slopes[key] = []
            self.__slopes[key].append(slope[key])

    def __analyze(self):
        pass
