from adapter.OdbAdapter import *
from processor.EventProcessor import *


def main():
    processor = EventProcessor()
    processor.process()

    # adapter = OdbAdapter()
    # print adapter.speed


main()
