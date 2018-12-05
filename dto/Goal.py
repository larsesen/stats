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
        self.minutes, self.seconds = get_time_in_minutes_and_seconds(time)

    def __str__(self):
        return "Result = {}, time = {}:{}, scorer = {}"\
            .format(self.partial_result, self.minutes, self.seconds, self.scorer)


def get_time_in_minutes_and_seconds(time):
    period, timestamp = time.split('-')

    minutes = int(timestamp.split(':')[0].strip())
    seconds = int(timestamp.split(':')[1].strip())

    period = int(period)
    while period > 1:
        minutes += 20
        period -= 1

    minutes = pretty_print_time(minutes)
    seconds = pretty_print_time(seconds)
    return minutes, seconds


def pretty_print_time(number):
    if number < 10:
        number = '0' + str(number)
    return number

