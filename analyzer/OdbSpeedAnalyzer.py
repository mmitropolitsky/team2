from analyzer.BaseAnalyzer import BaseAnalyzer


class OdbSpeedAnalyzer(BaseAnalyzer):

    def has_exception(self):
        print self.__class__
        return False
