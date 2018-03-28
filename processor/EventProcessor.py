import time

from analyzer.PostureAnalyzer import PostureAnalyzer


class EventProcessor(object):

    def process(self):
        while True:
            print 'invoking analyzers'
            print self.__invoke_analyzers()
            self.__invoke_analyzers()
            time.sleep(0.1)

    def __invoke_analyzers(self):
        a = PostureAnalyzer
        return a.has_exception()

