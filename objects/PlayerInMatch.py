class PlayerInMatch(object):
    name = ""
    shirt_number = 0
    is_captain = False
    goals = 0
    assists = 0
    points = 0
    penalties = 0
    actually_played_match = False

    def __init__(self, name, shirt_number, is_captain, goals, assists, points, penalties, category):
        self.name = unicode(name).encode('utf-8')
        self.shirt_number = shirt_number
        self.is_captain = is_captain
        self.goals = goals
        self.assists = assists
        self.points = points
        self.penalties = penalties
        self.actually_played_match = category

    def __str__(self):
        return '#{} {}, captain: {}\n#goals: {}\n#assists: {}\n#points: {}\n#penalties: {}\ncategory: {}' \
            .format(self.shirt_number, self.name, self.is_captain, self.goals, self.assists, self.points,
                    self.penalties, self.actually_played_match)
