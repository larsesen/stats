class TimeInPeriod(object):
    minutes = 0
    seconds = 0

    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "Minutes={}, seconds={}".format(self.minutes, self.seconds)


def makeTimeInPeriod(minutes, seconds):
    timeOfGoal = TimeInPeriod(minutes, seconds)
    return timeOfGoal
