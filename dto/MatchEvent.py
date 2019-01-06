import Constants
import TimeParseUtils


class MatchEvent(object):
    team = ""
    player = ""
    period = 0
    minutes = 0
    seconds = 0
    sort_stamp = 0


class Goal(MatchEvent):
    assist = ""
    partial_result = ""

    def __init__(self, scorer, assist, partial_result, team_name, time):
        self.player = unicode(clean_player_name(scorer)).encode('utf-8')
        self.assist = unicode(clean_player_name(assist)).encode('utf-8')
        self.partial_result = partial_result
        self.team = Constants.map_team_name_to_shortname.get(team_name)
        self.period = TimeParseUtils.get_period_number(time)
        self.minutes, self.seconds = TimeParseUtils.get_time_in_minutes_and_seconds(time)
        self.sort_stamp = get_sort_stamp(self.minutes, self.seconds)

    def __str__(self):
        separator = '|'
        return '{text: <{width}}'.format(text='Goal', width=7) + separator + \
               '{text: <{width}}'.format(text="time = " + str(self.minutes) + ":" + str(self.seconds) + separator, width=13) + \
               '{text: <{width}}'.format(text="team = " + self.team, width=33) + separator + \
               '{text: <{width}}'.format(text="scorer = " + self.player, width=50) + separator + \
               '{text: <{width}}'.format(text="partial result = " + self.partial_result, width=15)


class Penalty(MatchEvent):
    duration = ""
    reason = ""

    def __init__(self, team, time, penalty):
        self.team = unicode(team).encode('utf-8')
        self.period = TimeParseUtils.get_period_number(time)
        self.minutes, self.seconds = TimeParseUtils.get_time_in_minutes_and_seconds(time)
        self.sort_stamp = get_sort_stamp(self.minutes, self.seconds)
        self.player, self.duration, self.reason = get_player_info(penalty)

    def __str__(self):
        separator = '|'
        return ('{text: <{width}}'.format(text='Penalty' + separator, width=8) +
               '{text: <{width}}'.format(text="time = " + str(self.minutes) + ":" + str(self.seconds), width=12) + separator +
               '{text: <{width}}'.format(text="team = " + self.team, width=33) + separator +
               '{text: <{width}}'.format(text="player = " + self.player, width=50) + separator +
               '{text: <{width}}'.format(text="duration = " + str(self.duration), width=22) + separator +
               '{text: <{width}}'.format(text="reason = " + self.reason, width=50))


def get_sort_stamp(minutes, seconds):
    return int(minutes) * 60 + int(seconds)


def clean_player_name(player_name):
    score_line = player_name.split('.')
    length = len(score_line)
    if length == 1:
        return player_name
    return score_line[1].strip()


def clean_player_name_penalty(player_name):
    penalty_entry = player_name.split('.')
    return unicode(penalty_entry[1].strip()).encode('utf-8')


def get_player_info(penalty):
    player, duration, reason = penalty.split(',')
    return clean_player_name_penalty(player), extract_duration_of_penalty(duration), \
           unicode(reason.strip()).encode('utf-8')


def extract_duration_of_penalty(duration):
    return int(duration.strip().split(' ')[0].strip())
