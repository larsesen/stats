class MatchInfo(object):
    date = ""
    arena = ""
    away_team = ""
    home_team = ""
    result = ""

    def __init__(self, date, arena, home_team, away_team, result):
        self.date = date
        self.arena = arena
        self.home_team = home_team
        self.away_team = away_team
        self.result = result

    def __str__(self):
        return "Date: {}\nArena: {}\nHome team: {}\nAway team: {}\nResult: {}"\
            .format(self.date, self.arena, self.home_team, self.away_team, self.result)
