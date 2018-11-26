import json
from TimeOfGoal import makeTimeOfGoal

# Json-file has following fields
# Time
# PartialResult
# TeamName
# TeamUrl
# Scorer
# Assist
# IsPenaltyGoal
# IsOwnGoal
# IsHomeGoal


teamName = "TeamName"
BMIL = "BMIL Herrer 1"
timestamp = "Time"

def main():
    tidspunkter = []

    data = readJsonData("goalsInOrder.json")
    for goal in data:
        if goal[teamName] == BMIL:
            tidspunkt = goal["Time"]

            tidspunktMedPeriode = tidspunkt.split("-");
            periode = int(tidspunktMedPeriode[0]);

            minutterOgSekunder = tidspunktMedPeriode[1].strip().split(':')

            timestamp = makeTimeOfGoal(periode, minutterOgSekunder[0], minutterOgSekunder[1])
            tidspunkter.append(timestamp)

    printTimestamps(tidspunkter)


def readJsonData(pathToFile):
    with open(pathToFile) as json_data:
        data = json.load(json_data)
        return data

def printTimestamps(tidspunkter):
    for tidspunkt in tidspunkter:
        print tidspunkt


main()



#pprint(data)
