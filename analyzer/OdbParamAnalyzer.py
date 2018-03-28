from analyzer.BaseAnalyzer import BaseAnalyzer


class OdbParamAnalyzer(BaseAnalyzer):

    def has_exception(self):
        print self.__class__
        return False

