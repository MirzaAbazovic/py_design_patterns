import time

class Producer:
    """Resource intensive object to instantiate - protected object"""
    def produce(self):
        print('Producer is working hard')

    def meet(self):
        return 'Producer has time to meet You now'

class Proxy:
    """Less resource-intensive proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = True
        self.producer = None

    def produce(self):
        """check is Producer available  """
        print("Artist is checking if Producer is available ... ")

        if self.occupied:
            print("He is busy")
            #if producer is not available send some dummy data
            time.sleep(2)
            return "Producer is busy"
        else:
            #if producer is available create a producer object
            print("He is available")
            self.producer = Producer()
            time.sleep(2)
            #proxy method to producer
            return self.producer.meet()


