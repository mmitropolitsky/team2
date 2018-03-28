from processor.EventProcessor import *
from adapter.OdbAdapter import *


def main():
    #processor = EventProcessor()
    #processor.process()


    adapter = OdbAdapter()
    print adapter.speed


main()
