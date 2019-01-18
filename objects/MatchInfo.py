from Constants import MatchResult as MatchResult


class MatchInfo(object):
    date = ""
    arena = ""
    away_team = ""
    home_team = ""
    result = ""
    result_for_home_team = ""
    result_for_away_team = ""

    def __init__(self, date, arena, home_team, away_team, result):
        self.date = date
        self.arena = arena
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.result_for_home_team, self.result_for_away_team = get_result_for_match(self)

    def __str__(self):
        return "Date: {}\nArena: {}\nHome team: {}\nAway team: {}\nResult: {}"\
            .format(self.date, self.arena, self.home_team, self.away_team, self.result)


def get_result_for_match(match_info):
    match_details = match_info.result.split(' (')

    away_goal, home_goal = get_goals_for_home_and_away(match_details)
    result_per_period = get_results_per_period(match_info)

    if len(result_per_period) == 3:
        if home_goal > away_goal:
            return MatchResult.WIN, MatchResult.LOSS
        elif home_goal < away_goal:
            return MatchResult.LOSS, MatchResult.WIN

    else:
        if home_goal > away_goal:
            return MatchResult.WIN_PEN, MatchResult.LOSS_PEN
        elif home_goal < away_goal:
            return MatchResult.LOSS_PEN, MatchResult.WIN_PEN
    raise ValueError("Not possible result")


def get_goals_for_home_and_away(match_details):
    home_goal, away_goal = match_details[0].split('-')
    return int(away_goal), int(home_goal)


def get_results_per_period(match_info):
    period_results = match_info.result.split('(')[1].replace(')', "")
    result_per_period = period_results.split(',')
    return result_per_period
