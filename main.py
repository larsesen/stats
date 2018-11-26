from RetrieveDataFromFile import *
from dto.Match import getGoalTimeInSeconds

from PlotHistogram import getPlot


def getGoalTimestampsForMatch():
    #TODO: Traverse all files in directory "goalFiles"
    #TODO: Object with goals is contained in object named goalsInOrderVM. Provide only linkid from main for result page and retrieve automatically

    timestampsFirst = getTimestampsForGoals("goalFiles/20180916_lyn_bmil.json")
    timestampsSecond = getTimestampsForGoals("goalFiles/20180922_bmil_grei.json")
    timeStampsThird = getTimestampsForGoals("goalFiles/20180930_lsk_bmil.json")

    timeStampsFourth = getTimestampsForGoals("goalFiles/20181003_bmil_ajer.json")
    timeStampsFifth = getTimestampsForGoals("goalFiles/20181014_ullkisa_bmil.json")
    timeStampsSixth = getTimestampsForGoals("goalFiles/20181027_bmil_oreasen.json")

    timeStampsSeventh = getTimestampsForGoals("goalFiles/20181104_vif_bmil.json")
    timeStampsEighth = getTimestampsForGoals("goalFiles/20181117_bmil_lyn.json")
    timeStampsNinth = getTimestampsForGoals("goalFiles/20181124_grei_bmil.json")


    #print "Timestamps in match: "
    allGoals = timestampsFirst + timestampsSecond + timeStampsThird + \
               timeStampsFourth + timeStampsFifth + timeStampsSixth + \
               timeStampsSeventh + timeStampsEighth + timeStampsNinth
    #printTimestamps(allGoals)

    print "\nTotal of {} goals scored".format(len(allGoals))

    return allGoals


#TODO: Clean names and variables into methods
goalsInSeconds = getGoalTimeInSeconds(getGoalTimestampsForMatch())
plot = getPlot(goalsInSeconds)
plot.show()
