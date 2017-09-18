import datetime

class Task(object):
    """A task to represent a unit of activity over a time period.

    Ideally a task should have a title and duration and the scheduler handles when and where to put it.

    A task is something that needs to be done there and then.
    """

    def __init__(self, title='Default Task', duration=30, starttime=datetime.time()):
        self.title = title
        self.duration = datetime.timedelta(minutes=duration)
        self.complete = False

        # Optional
        self.starttime = starttime

    def info(self):
        print '##############################'
        print 'Title: %s' % self.title
        print 'Duration: %s' % self.duration
        print '##############################'

    def fixed(self):
        return bool(self.starttime)
