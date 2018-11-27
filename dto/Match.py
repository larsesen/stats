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

    def get_period(self):
        return self.period

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds


def make_timestamp_in_match(period, minutes, seconds):
    time_of_goal = TimeInMatch(period, minutes, seconds)
    return time_of_goal


def get_goal_time_in_seconds(goals):
    timestamps_in_seconds = []
    for goal in goals:
        if goal is not None:
            period = goal.get_period()
            minutes = goal.get_minutes()
            seconds = goal.get_seconds()

            time_in_seconds = ((int(period) -1) * 20 * 60) + (int(minutes) * 60) + int(seconds)

            timestamps_in_seconds.append(time_in_seconds)
    timestamps_in_seconds.sort()
    return timestamps_in_seconds
