

class Scheduler(object):
    """This organised tasks into a optimised format.

    Ideally the scheduler should know how and when to schedule tasks based on importance.
    """

    def __init__(self, tasks):
        self.tasks = tasks
        self.schedulingStrategy = self._getSchedulingStrategy()

    def _getSchedulingStrategy(self):
            return ''

    def carriedTasks(self):
        """This works out what tasks have been carried over from previous days.

        Maybe there needs to be a re-ordering here to get these tasks complete.
        """



def schedule(tasks):

    if not tasks:
        # TODO Think of a better way to handle no tasks.
        print 'There are no tasks to schedule'

    shed = Scheduler(tasks)
    shed.schedule()