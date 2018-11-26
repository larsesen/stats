from ReadFile import readJsonData

from dto.Match import makeTimeInMatch
from dto.Period import makeTimeInPeriod

from GoalConstants import AccessObjects


BMIL = "BMIL Herrer 1"


def getTimestampsForGoals(path):
    first = readJsonData(path)
    timestampsSecond = getTimestampsInMatch(first)
    return timestampsSecond


def getTimestampsInMatch(data):
    timestamps = []
    for goal in data:
        if goal[AccessObjects.TeamName] == BMIL:
            timestamps.append(createMatchTimestamp(goal))
    return timestamps


def getTimestampsInPeriod(data):
    timestamps = []
    for goal in data:
        if goal[AccessObjects.TeamName] == BMIL:
            matchTimeStamp = createMatchTimestamp(goal)
            timestamps.append(makeTimeInPeriod(matchTimeStamp.minutes, matchTimeStamp.seconds))
    return timestamps


def createMatchTimestamp(goal):
    time = goal[AccessObjects.Time]

    if time == "Str":
        return
    timeAndPeriod = time.split("-")
    period = int(timeAndPeriod[0])
    minutesAndSeconds = timeAndPeriod[1].strip().split(':')
    timestamp = makeTimeInMatch(period, minutesAndSeconds[0], minutesAndSeconds[1])
    return timestamp


def printTimestamps(tidspunkter):
    for tidspunkt in tidspunkter:
        print tidspunkt
