from scheduler.calendar import Day


class Strategy(object):
    """A strategy to organise tasks into a period of time.

    A strategy should be aware of the time period to schedule tasks in
    and also tasks that are needing to be scheduled.
    """

    def __init__(self, tasks=[], day=None):
        self.day = day or Day()
        self.tasks = tasks

    def name(self):
        return 'base'

    def details(self):
        return 'This is the base class for strategies. Inherit this class into a strategy'

    def organise(self):
        raise BaseException('Strategies should over write this method to organise.')
