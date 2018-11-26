from ReadFile import readJsonData

from dto.Match import makeTimestampInMatch
from dto.Period import makeTimeInPeriod

from GoalConstants import GoalAccessObjects


BMIL = "BMIL Herrer 1"


def getTimestampsForGoals(path):
    first = readJsonData(path)
    timestampsSecond = getTimestampsInMatch(first)
    return timestampsSecond


def getTimestampsInMatch(data):
    timestamps = []
    for goal in data:
        if goal[GoalAccessObjects.TeamName] == BMIL:
            timestamps.append(createMatchTimestamp(goal))
    return timestamps


def getTimestampsInPeriod(data):
    timestamps = []
    for goal in data:
        if goal[GoalAccessObjects.TeamName] == BMIL:
            matchTimeStamp = createMatchTimestamp(goal)
            timestamps.append(makeTimeInPeriod(matchTimeStamp.minutes, matchTimeStamp.seconds))
    return timestamps


def createMatchTimestamp(goal):
    time = goal[GoalAccessObjects.Time]

    if time == "Str": #no timestamp for penalty shootout
        return
    timeAndPeriod = time.split("-")
    period = int(timeAndPeriod[0])
    minutesAndSeconds = timeAndPeriod[1].strip().split(':')
    timestamp = makeTimestampInMatch(period, minutesAndSeconds[0], minutesAndSeconds[1])
    return timestamp


def printTimestamps(tidspunkter):
    for tidspunkt in tidspunkter:
        if tidspunkt is not None:
            print tidspunkt
