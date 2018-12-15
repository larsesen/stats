import TimeParseUtils


class Penalty(object):
    team = ""
    player = ""
    period = ""
    minutes = 0
    seconds = 0
    duration = ""
    reason = ""

    def __init__(self, team, time, penalty):
        self.team = team
        self.period = TimeParseUtils.get_period_number(time)
        self.minutes, self.seconds = TimeParseUtils.get_time_in_minutes_and_seconds(time)
        self.player, self.duration, self.reason = get_player_info(penalty)

    def __str__(self):
        return "Penalty: team: {}, time = {}:{}, player = {}, duration = {}, reason: {}" \
            .format(self.team, self.minutes, self.seconds, self.player, self.duration, self.reason)


def get_player_info(penalty):
    player, duration, reason = penalty.split(',')
    return player.strip(), duration.strip(), reason.strip()
