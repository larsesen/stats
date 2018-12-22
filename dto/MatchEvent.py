import Constants
import TimeParseUtils


class MatchEvent(object):
    team = ""
    period = 0
    minutes = 0
    seconds = 0
    sort_stamp = 0


class Goal(MatchEvent):
    scorer = ""
    assist = ""
    partial_result = ""

    def __init__(self, scorer, assist, partial_result, team_name, time):
        self.scorer = clean_scorer(scorer)
        self.assist = assist
        self.partial_result = partial_result
        self.team = Constants.map_team_name_to_shortname.get(team_name)
        self.period = TimeParseUtils.get_period_number(time)
        self.minutes, self.seconds = TimeParseUtils.get_time_in_minutes_and_seconds(time)
        self.sort_stamp = get_sort_stamp(self.period, self.minutes, self.seconds)

    def __str__(self):

        separator = '|'
        return '{text: <{width}}'.format(text='Goal', width=7) + separator + \
               '{text: <{width}}'.format(text="time = " + str(self.minutes) + ":" + str(self.seconds) + separator, width=13) + \
               '{text: <{width}}'.format(text="team = " + self.team, width=33) + separator + \
               '{text: <{width}}'.format(text="scorer = " + self.scorer, width=50) + separator + \
               '{text: <{width}}'.format(text="partial result = " + self.partial_result, width=15)


class Penalty(MatchEvent):
    player = ""
    duration = ""
    reason = ""

    def __init__(self, team, time, penalty):
        self.team = team
        self.period = TimeParseUtils.get_period_number(time)
        self.minutes, self.seconds = TimeParseUtils.get_time_in_minutes_and_seconds(time)
        self.sort_stamp = get_sort_stamp(self.period, self.minutes, self.seconds)
        self.player, self.duration, self.reason = get_player_info(penalty)

    def __str__(self):
        separator = '|'
        return '{text: <{width}}'.format(text='Penalty' + separator, width=8) + \
               '{text: <{width}}'.format(text="time = " + str(self.minutes) + ":" + str(self.seconds), width=12) + separator + \
               '{text: <{width}}'.format(text="team = " + self.team, width=33) + separator +  \
               '{text: <{width}}'.format(text="player = " + self.player, width=50) + separator +  \
               '{text: <{width}}'.format(text="duration = " + self.duration, width=22) + separator + \
               '{text: <{width}}'.format(text="reason = " + self.reason, width=50)


def get_sort_stamp(period, minutes, seconds):
    return int(str(period) + "" + str(minutes) + "" + str(seconds))


def clean_scorer(scorer):
    score_line = scorer.split('.')
    length = len(score_line)
    if length == 1:
        return scorer
    return score_line[1].strip()


def get_player_info(penalty):
    player, duration, reason = penalty.split(',')
    return player.strip(), duration.strip(), reason.strip()
