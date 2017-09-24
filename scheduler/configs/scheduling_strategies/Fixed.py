"""This Fixed strategy attempts to add tasks with a fixed starttime."""
from base import Strategy


class Fixed(Strategy):

    def __init__(self, *args, **kwargs):
        super(Fixed, self).__init__(*args, **kwargs)

    def name(self):
        return 'Fixed'

    def details(self):
        return 'A Fixed organisation strategy. Schedule fixed tasks.'

    def organise(self):
        """Firstly put in the tasks by starttime then other tasks in around that."""
        self.sort_tasks(self.tasks_to_organise())
        self.organise_todo()

    def organise_todo(self):
        for task in self.day.todo:
            print 'Adding: ', task.title
            self.day.next_available_slot(task)


    def tasks_to_organise(self):
        """Only organise tasks that have a fixed starttime.

        Other tasks should be added to the day but not in TODO.
        """
        # [self.task.pop(self.tasks.index(task)) for task in self.tasks if not task.fixed()]
        for task in self.tasks:
            if task.fixed():
                self.day.add_task_todo(task)
            else:
                self.day.add_task(task)

        print 'Tasks:', self.day.todo
        return self.day.todo

    def sort_tasks(self, tasks):

        def _getKey(obj):
                return obj.starttime

        return sorted(tasks, key=_getKey)
