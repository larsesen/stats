class PlayerInMatch(object):
    name = ""
    shirt_number = 0
    is_captain = False
    goals = 0
    assists = 0
    points = 0
    penalties = 0

    def __init__(self, name, shirt_number, is_captain, goals, assists, points, penalties):
        self.name = unicode(name).encode('utf-8')
        self.shirt_number = shirt_number
        self.is_captain = is_captain
        self.goals = goals
        self.assists = assists
        self.points = points
        self.penalties = penalties

    def __str__(self):
        return '#{} {}, captain: {}\n#goals: {}\n#assists: {}\n#points: {}\n#penalties: {}' \
            .format(self.shirt_number, self.name, self.is_captain, self.goals, self.assists, self.points,
                    self.penalties)
