def print_league_table(data_for_season):
    print 'Team \t\t  K  S  US UT T  Goals  +-  P'
    print '--------------------------------------------'
    for season in sorted(data_for_season, key=lambda x: x.points, reverse=True):
        print season


def print_team_statistics(season):
    print 'Top scorers:'
    print print_entries_sorted(season.top_scorers)
    print '\n------------------\n'
    print 'Assists:'
    print print_entries_sorted(season.assists)
    print '\n------------------\n'
    print 'Penalties:'
    print print_entries_sorted(season.penalties_per_player)


def print_entries_sorted(match_events):
    s = ""
    for key, value in sorted(match_events.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        s += '\n' + key + ": " + str(value)
    print s
