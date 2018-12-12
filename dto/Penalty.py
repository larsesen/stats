class Penalty(object):
    team = ""
    player = ""
    minutes = 0
    seconds = 0
    duration = ""
    reason = ""

    def __init__(self, team, time, penalty):
        self.team = team
        self.minutes, self.seconds = get_time_in_minutes_and_seconds(time)
        self.player, self.duration, self.reason = get_player_info(penalty)

    def __str__(self):
        return "Penalty: team: {}, time = {}:{}, player = {}, duration = {}, reason: {}" \
            .format(self.team, self.minutes, self.seconds, self.player, self.duration, self.reason)


# todo This should use same logic as in Goal.py -> Extract
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


# todo This should use same logic as in Goal.py -> Extract
def pretty_print_time(number):
    if number < 10:
        number = '0' + str(number)
    return number


def get_player_info(penalty):
    player, duration, reason = penalty.split(',')
    return player.strip(), duration.strip(), reason.strip()
