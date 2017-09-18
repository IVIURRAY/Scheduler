"""This FIFO strategy attempts to plan strategies in a first in, first out order."""
from base import Strategy


class FIFO(Strategy):

    def __init__(self):
        super(FIFO, self).__init__()

    def name(self):
        return 'FIFO'

    def details(self):
        return 'A FIFO organisation strategy. First in, first out.'

    def organise(self, tasks):
        """Firstly put in the tasks by starttime then other tasks in around that."""


        for task in self.tasks:
            task
