"""These configs are here incase we exspand out.

IDEAS:
    1) Maybe split configs into priotry. Tasks we must, should and could do.
    2) Maybe split configs into events, gym / work / social / family etc...


"""
import datetime


TASKS = [
    dict(
        title='Sleeping',
        duration=420,
    ),

    dict(
        title='Breakfast',
        duration=15,
    ),

    dict(
        title='Commute',
        duration=45,
    ),

    dict(
        title='Work-morning',
        starttime=datetime.time(9),
        duration=45,
    ),

    dict(
        title='Gym',
        starttime=datetime.time(13),
        duration=80,
    ),

    dict(
        title='Work-afternoon',
        duration=300,
    ),

    dict(
        title='Comute Home',
        duration=60,
    ),

    dict(
        title='Dinner',
        duration=90,
    ),

    dict(
        title='Wash',
        duration=30,
    ),

    dict(
        title='Bedtime',
        duration=300,
    )
]