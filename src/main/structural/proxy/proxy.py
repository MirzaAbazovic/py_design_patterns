import time

class Producer:
    """Resouce intensive object to instanciate - protected object"""

    def produce(self):
        print('Producer is working hard')

    def meet(self):
        print('Producer has time to work for You now')

class Proxy:
    """Less resource-intensive """