from ReadFile import readJsonData
from RetrieveDataFromFile import *


def main():

    #TODO: Object with goals is contained in object named goalsInOrderVM. Provide linkid for result page and retrieve automatically
    #TODO: Convert timestamps to seconds
    #TODO: PLOT graph (showing every minute?)

    timestampsFirst = getTimestampsForGoals("goalFiles/20180916_lyn_bmil.json")
    timestampsSecond = getTimestampsForGoals("goalFiles/20180922_bmil_grei.json")
    timeStampsThird = getTimestampsForGoals("goalFiles/20180930_lsk_bmil.json")

    timeStampsFourth = getTimestampsForGoals("goalFiles/20181003_bmil_ajer.json")
    timeStampsFifth = getTimestampsForGoals("goalFiles/20181014_ullkisa_bmil.json")
    timeStampsSixth = getTimestampsForGoals("goalFiles/20181027_bmil_oreasen.json")

    timeStampsSeventh = getTimestampsForGoals("goalFiles/20181104_vif_bmil.json")
    timeStampsEighth = getTimestampsForGoals("goalFiles/20181117_bmil_lyn.json")
    timeStampsNinth = getTimestampsForGoals("goalFiles/20181124_grei_bmil.json")


    print "Timestamps in match: "
    allGoals = timestampsFirst + timestampsSecond + timeStampsThird + \
               timeStampsFourth + timeStampsFifth + timeStampsSixth + \
               timeStampsSeventh + timeStampsEighth + timeStampsNinth
    printTimestamps(allGoals)

    print "\nTotal of {} goals scored".format(len(allGoals))




main()