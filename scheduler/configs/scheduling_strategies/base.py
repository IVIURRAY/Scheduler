from scheduler.calendar import Day


class Strategy(object):
    """A strategy to organise tasks into a period of time.

    A strategy should be aware of the time period to schedule tasks in
    and also tasks that are needing to be scheduled.
    """

    def __init__(self, day=None):
        self.day = day or Day()
        self.tasks = []

    def name(self):
        return 'base'

    def details(self):
        return 'This is the base class for strategies. Inherit this class into a strategy'

    def handle_fixed_tasks(self):
        """For any tasks with a fixed starttime we should handle these first."""
        for task in self.tasks:
            if task.fixed():
                self.day.add_task_todo(task)

    def _check_fixed_tasks(self, day):
        m = dict()
        for task in self.day.todo:
            # Need to map starttime to duration and make sure none cross over.
            # maybe this would be best handled to the slot


    def organise(self):
        raise BaseException('Strategies should over write this method to organise.')
