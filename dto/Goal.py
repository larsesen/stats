class Goal(object):
    scorer = ""
    assist = ""
    partial_result = ""
    team_name = ""
    time = ""
    period = ""
    timestamp = ""

    def __init__(self, scorer, assist, partial_result, team_name, time):
        # type: (String, String, String, String, String) -> Goal
        self.scorer = scorer
        self.assist = assist
        self.partial_result = partial_result
        self.team_name = team_name
        self.period = time.split('-')[0].strip()
        self.timestamp = time.split('-')[1].strip()

    def __str__(self):
        return "Result = {}, period = {}, time = {} scorer = {}"\
            .format(self.partial_result, self.period, self.timestamp, self.scorer)
