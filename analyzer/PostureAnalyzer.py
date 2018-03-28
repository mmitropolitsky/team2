from analyzer.BaseAnalyzer import BaseAnalyzer


class PostureAnalyzer(BaseAnalyzer):
    def has_exception(self):
        return not self.__is_person_in_frame()

    def __is_person_in_frame(self):
        print 'here'
        # some code here
        return True
