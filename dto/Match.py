class TimeInMatch(object):
    period = 0
    minutes = 0
    seconds = 0

    def __init__(self, period, minutes, seconds):
        self.period = period
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "period={0}, minutes={1}, seconds={2}".format(self.period, self.minutes, self.seconds)

    def getPeriod(self):
        return self.period

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

def makeTimestampInMatch(period, minutes, seconds):
    time_of_goal = TimeInMatch(period, minutes, seconds)
    return time_of_goal


def getGoalTimeInSeconds(goals):
    timestampsInSeconds = []
    for goal in goals:
        if goal is not None:
            period = goal.getPeriod()
            minutes = goal.getMinutes()
            seconds = goal.getSeconds()

            timeInSeconds = ((int(period) -1) * 20 * 60) + (int(minutes) * 60) + int(seconds)

            timestampsInSeconds.append(timeInSeconds)
    timestampsInSeconds.sort()
    return timestampsInSeconds;
