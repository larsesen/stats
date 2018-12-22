from collections import Counter


def get_goals_grouped_by_player(goals):
    scorers = []
    for goal in goals:
        scorers.append(goal.scorer)
    counter = Counter(scorers)

    for key, value in sorted(counter.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        print "%s: %s" % (key, value)


class Season(object):
    team_name = ""
    matches = []
    goals_for = []
    goals_against = []
    penalties = []

    def __init__(self, team_name, matches):
        self.team_name = team_name
        self.matches = matches
        self.goals_for = get_goals_for(self, matches)
        self.goals_against = get_goals_against(self, matches)
        self.penalties = get_penalties(self, matches)

    def __str__(self):
        return "Team name : {}" \
               "\nNumber of matches: {}" \
               "\nnumber of goals scored: {}" \
               "\nNumber of goals conceeded: {}" \
               "\nnumber of penalties: {}"\
            .format(self.team_name, len(self.matches), len(self.goals_for), len(self.goals_against), len(self.penalties))


def get_penalties(self, matches):
    penalties = []

    for match in matches:
        for penalty in match.penalties:
            if penalty.team == self.team_name:
                penalties.append(penalty)
    return penalties


def get_goals_for(self, matches):
    goals = []
    for match in matches:
        for goal in match.goals:
            if goal.team == self.team_name:
                goals.append(goal)
    return goals


def get_goals_against(self, matches):
    goals = []
    for match in matches:
        for goal in match.goals:
            if goal.team != self.team_name:
                goals.append(goal)
    return goals
