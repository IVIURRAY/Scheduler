import datetime

class Calendar(object):
    pass

class Month(Calendar):
    pass

class Week(Month):
    pass


class Day(Week):
    """A day is a representation of a 24hr period.

    Days should store tasks that want to be completed for this day.
    """

    def __init__(self):
        self.tasks = []     # A collection of all tasks that want to be performed.
        self.todo = []      # Actual tasks that will be done today.

    def todo(self):
        # return tasks to do today
        return self.todo

    def add_task_todo(self, task):
        self.todo.append(task)

    def add_tasks(self, tasks):
            [self.add_task(task) for task in tasks]

    def add_task(self, task):
        """Add a task to be completed"""
        self.tasks.append(task)

    def remove_tasks(self, tasks):
        [self.remove_tasks(task) for task in tasks]

    def remove_task(self, task):
        self.tasks.pop(self.tasks.index(task)) if task in self.tasks else None

    def next_available_slot(self):
        """Return the next available time slot"""
        slots = []
        for slot in self.available_slots():
            slots.append(slot)

        return slots.sort('time')[0]

    def available_slots(self):
        """Return the next available time slot"""
        return []


class Slot(object):
    """This is a representation of a block of time that can be used to schedule tasks.

    Similar to in Microsoft Outlook where you block time into your calendar.
    """

    def __init__(self, task, start, duration):
        self.task = task
        self.start = start
        self.duration = duration
        self.end = self.start + datetime.timedelta(duration.hour, duration.minute)

    def slot(self):
        return dict(
            title=self.task.title,
            task_obj=self.task,
            start=self.start,
            end=self.end,
        )