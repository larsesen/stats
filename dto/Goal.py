import TimeParseUtils


class Goal(object):
    scorer = ""
    assist = ""
    partial_result = ""
    team_name = ""
    time = ""
    period = ""
    timestamp = ""
    minutes = 0
    seconds = 0

    def __init__(self, scorer, assist, partial_result, team_name, time):
        # type: (String, String, String, String, String) -> Goal
        self.scorer = scorer
        self.assist = assist
        self.partial_result = partial_result
        self.team_name = team_name
        self.period = TimeParseUtils.get_period_number(time)
        self.minutes, self.seconds = TimeParseUtils.get_time_in_minutes_and_seconds(time)

    def __str__(self):
        return "Goal: {}, time = {}:{}, scorer = {}"\
            .format(self.partial_result, self.minutes, self.seconds, self.scorer)
