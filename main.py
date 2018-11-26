from ReadFile import readJsonData
from RetrieveDataFromFile import *


def main():
    data = readJsonData("goalFiles/20181124_grei_bmil.json")

    print "Timestamps in match: "
    timestamps = getTimestampsInMatch(data)
    printTimestamps(timestamps)

    print "\n\n"
    print "Timestamps in period: "
    periodTimeStamps = getTimestampsInPeriod(data)
    printTimestamps(periodTimeStamps)

main()