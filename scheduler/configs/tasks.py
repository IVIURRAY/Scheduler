"""These configs are here incase we exspand out.

IDEAS:
    1) Maybe split configs into priotry. Tasks we must, should and could do.
    2) Maybe split configs into events, gym / work / social / family etc...


"""
import datetime
from scheduler.task import Task

TASKS = [
    Task(
        title='Sleeping',
        duration=420,
    ),

    Task(
        title='Breakfast',
        duration=15,
    ),

    Task(
        title='Commute',
        duration=45,
    ),

    Task(
        title='Work-morning',
        starttime=datetime.time(9),
        duration=45,
    ),

    Task(
        title='Gym',
        starttime=datetime.time(13),
        duration=80,
    ),

    Task(
        title='Work-afternoon',
        duration=300,
    ),

    Task(
        title='Comute Home',
        duration=60,
    ),

    Task(
        title='Dinner',
        duration=90,
    ),

    Task(
        title='Wash',
        duration=30,
    ),

    Task(
        title='Bedtime',
        duration=300,
    )
]