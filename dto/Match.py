import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Match(object):
    match_info = {}
    goals = []
    penalties = []

    def __init__(self, match_info, goals, penalies):
        self.match_info = match_info
        self.goals = goals
        self.penalties = penalies


# todo Put all goals and penalties in a single list and sort. Divide statistics by period
    def __str__(self):
        match_report = "Date: {}\nArena: {}\nHome team: {}\nAway team: {}\nResult: {}\n" \
            .format(self.match_info.date, self.match_info.arena, self.match_info.home_team, self.match_info.away_team,
                    self.match_info.result)
        for goal in self.goals:
            match_report += goal.__str__() + "\n"
        for penalty in self.penalties:
            match_report += penalty.__str__() + "\n"
        return match_report
