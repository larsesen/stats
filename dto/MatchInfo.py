class MatchInfo(object):
    match_date = ""
    arena = ""
    away_team = ""
    end_result = ""
    home_team = ""

    def __init__(self, match_date, arena, home_team, away_team, end_result):
        self.match_date = match_date
        self.arena = arena
        self.home_team = home_team
        self.away_team = away_team
        self.end_result = end_result

    def __str__(self):
        return "Date: {}\nArena: {}\nHome team: {}\nAway team: {}\nResult: {}"\
            .format(self.match_date, self.arena, self.home_team, self.away_team, self.end_result)
