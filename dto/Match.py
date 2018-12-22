import sys

reload(sys)
sys.setdefaultencoding('utf8')


def find_goals_for_team(goals, team_name):
    goals_for_team = []
    for goal in goals:
        if goal.team == team_name:
            goals_for_team.append(goal)

    return goals_for_team


def find_penalties_for_team(penalties, team_name):
    team_penalties = []
    for penalty in penalties:
        if penalty.team == team_name:
            team_penalties.append(penalty)
    return team_penalties


class Match(object):
    match_info = {}
    all_goals = []
    all_penalties = []
    home_team = ""
    home_match_events = []
    home_penalties = []
    away_team = ""
    away_goals = []
    away_penalties = []

    def __init__(self, match_info, goals, penalties):
        self.match_info = match_info
        self.home_team = match_info.home_team
        self.all_goals = goals
        self.all_penalties = penalties
        self.home_goals = find_goals_for_team(goals, self.home_team)
        self.away_team = match_info.away_team
        self.home_penalties = find_penalties_for_team(penalties, self.home_team)
        self.away_goals = find_goals_for_team(goals, self.away_team)
        self.away_penalties = find_penalties_for_team(penalties, self.away_team)

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
        for goal in self.all_goals:
            match_events.append(goal)
        for penalty in self.all_penalties:
            match_events.append(penalty)

        match_events.sort(key=lambda x: x.sort_stamp)
        return match_events
