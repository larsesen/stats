def print_league_table(data_for_season):
    print 'Team \t\t  K  S  US UT T  Goals  +-  P'
    print '--------------------------------------------'
    for season in sorted(data_for_season, key=lambda x: x.points, reverse=True):
        print season
