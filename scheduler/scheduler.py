from scheduler.configs.scheduling_strategies.Fixed import Fixed
from scheduler.configs.tasks import TASKS
from scheduler.calendar import Day


class Scheduler(object):
    """This organised tasks into a optimised format.

    Ideally the scheduler should know how and when to schedule tasks based on importance.
    """

    def __init__(self, strategy, day=None):
        self.strategy = strategy
        self.day = day or Day()

    # def carriedTasks(self):
    #     """This works out what tasks have been carried over from previous days.
    #
    #     Maybe there needs to be a re-ordering here to get these tasks complete.
    #     """

    def schedule(self):
        self.day.apply_strategy(self.strategy)


def schedule():
    shed = Scheduler(Fixed(tasks=TASKS))
    shed.schedule()


# Request(
#     strategy='',
#     # tasks
#     # day=''
# )