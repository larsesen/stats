class TimeOfGoal(object):
    period = 0
    minutes = 0
    seconds = 0

    def __init__(self, period, minutes, seconds):
        self.period = period
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "period={0}, minutes={1}, seconds={2}".format(self.period, self.minutes, self.seconds)

def makeTimeOfGoal(period, minutes, seconds):
    timeOfGoal = TimeOfGoal(period, minutes, seconds)
    return timeOfGoal
