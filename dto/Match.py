import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Match(object):
    home_team = ""
    away_team = ""
    goals = []

    def __init__(self, home_team, away_team, goals):
        self.home_team = home_team
        self.away_team = away_team
        self.goals = goals

    def __str__(self):
        match_report = "Home team = {} \nAway team = {}\n".format(self.home_team, self.away_team)
        for goal in self.goals:
            match_report += goal.__str__() + "\n"
        return match_report
