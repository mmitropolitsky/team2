from scipy import stats
import numpy as np
import math
import json

from analyzer.BaseAnalyzer import BaseAnalyzer
from adapter.ObdAdapter import ObdAdapter


class ObdParamsAnalyzer(BaseAnalyzer):

    OBD_PARAMS = ['speed', 'throttle_pos', 'rpm', 'maf']
    MIN_LAST_ENTRIES_COUNT = 50

    def __init__(self):
        self.__adapter = ObdAdapter()
        self.__log_entries = []
        self.__slopes = dict()
        self.__log_entry = None
        self.__current_typical = json.load(open('data.json'))
        self.__last_ten_entries = []
        self.__last_ten_slopes = []

    def has_exception(self):
        return not self.__is_typical()

    def __is_typical(self):
        self.__log_entry, slope = self.__adapter.get_log_entry_and_slopes(self.__log_entry)
        self.__log_entries.append(self.__log_entry)
        self.__add_slope(slope)

        if len(self.__log_entries) < self.MIN_LAST_ENTRIES_COUNT:
            return True

        tmp_slopes = dict()

        for key in self.__slopes:
            tmp_slopes[key] = self.__slopes[key][-self.MIN_LAST_ENTRIES_COUNT:]

        last_ten_summary = self.__get_summary(self.__log_entries[-self.MIN_LAST_ENTRIES_COUNT:], tmp_slopes)
        for key in last_ten_summary:
            if key not in self.__current_typical:
                continue
            try:
                delta = abs(((float(last_ten_summary[key])-self.__current_typical[key])/self.__current_typical[key]))*100
                if delta > 10:
                    return False
            except ZeroDivisionError:
                continue
        return True

    def __add_slope(self, slope):
        for key in slope:
            if not key in self.__slopes:
                self.__slopes[key] = []
            self.__slopes[key].append(slope[key])

    def finalize(self):
        summary = self.__get_summary(self.__log_entries, self.__slopes)
        self.__persist(summary)

    def __get_summary(self, log_entries, slopes):
        summary = dict()
        for key in self.OBD_PARAMS:
            numbers = map(lambda entry: entry['speed'], log_entries)

            summary['avg_' + key] = np.average(numbers)
            summary['nintyth_per_' + key] = np.percentile(numbers, 90)

            for slope_direction in ['_increasing', '_decreasing']:
                if not (key + slope_direction) in slopes:
                    continue
                slope_vals = map(lambda entry: entry['value'], slopes[key + slope_direction])
                slope_timestamps = map(lambda entry: entry['value'], slopes[key + slope_direction])
                res = stats.linregress(slope_vals, slope_timestamps)
                if not math.isnan(res.slope):
                    summary[key + slope_direction] = res.slope

        return summary

    def __persist(self, summary):
        new_typical = dict()
        for key in summary:
            if key in self.__current_typical:
                val = (summary[key] + self.__current_typical[key])/2
            else:
                val = summary[key]
            new_typical[key] = val
        with open('data.json', 'w') as outfile:
            json.dump(new_typical, outfile)



