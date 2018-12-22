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

    def __str__(self):
        match_report = "Date: {}\nArena: {}\nHome team: {}\nAway team: {}\nResult: {}\n" \
            .format(self.match_info.date, self.match_info.arena, self.match_info.home_team, self.match_info.away_team,
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
