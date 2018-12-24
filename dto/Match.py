from Helper import MatchResult as MatchResult


class Match(object):
    match_info = {}
    home_team = ""
    away_team = ""
    goals = []
    penalties = []
    result_for_home_team = ""

    def __init__(self, match_info, goals, penalties):
        self.match_info = match_info
        self.home_team = match_info.home_team
        self.away_team = match_info.away_team
        self.goals = goals
        self.penalties = penalties
        self.result_for_home_team = get_result_for_home_team(match_info)

    def __str__(self):
        match_report = "Date: {}\nArena: {}\nHome team: {}\nAway team: {}\nResult: {}\n" \
            .format(self.match_info.date, self.match_info.arena, self.home_team, self.away_team,
                    self.match_info.result)

        match_report += self.get_printed_match_events()
        return match_report

    def get_printed_match_events(self):
        match_events = self.get_match_events_sorted()
        text = ""
        text += "\nMatch events:"
        period = 0
        for match_event in match_events:
            event_period = match_event.period
            if event_period > period:
                text += "\n-----period {}------\n".format(period + 1)
                period = event_period

            text += match_event.__str__() + "\n"
        text += "\nMatch end \n--------\n--------\n"
        return text

    def get_match_events_sorted(self):
        match_events = []
        for goal in self.goals:
            match_events.append(goal)
        for penalty in self.penalties:
            match_events.append(penalty)

        match_events.sort(key=lambda x: x.sort_stamp)
        return match_events


def get_result_for_home_team(match_info):
    match_details = match_info.result.split(' (')

    away_goal, home_goal = get_goals_for_home_and_away(match_details)
    result_per_period = get_results_per_period(match_info)

    if len(result_per_period) == 3:
        if home_goal > away_goal:
            return MatchResult.WIN
        elif home_goal < away_goal:
            return MatchResult.LOSS

    else:
        if home_goal > away_goal:
            return MatchResult.WIN_PEN
        elif home_goal < away_goal:
            return MatchResult.LOSS_PEN
    raise ValueError("Not possible result")


def get_goals_for_home_and_away(match_details):
    home_goal, away_goal = match_details[0].split('-')
    return int(away_goal), int(home_goal)


def get_results_per_period(match_info):
    period_results = match_info.result.split('(')[1].replace(')', "")
    result_per_period = period_results.split(',')
    return result_per_period
