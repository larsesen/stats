def print_league_table(data_for_season):
    print 'Team \t\t  K  S  US UT T  Goals  +-  P'
    print '--------------------------------------------'
    for season in sorted(data_for_season, key=lambda x: x.find_number_of_points(), reverse=True):
        print season


def print_team_statistics(season):
    print 'Top scorers:'
    print print_entries_sorted(season.get_goals_grouped_by_player())
    print '\n------------------\n'
    print 'Assists:'
    print print_entries_sorted(season.get_assists_by_player())
    print '\n------------------\n'
    print 'Penalties:'
    print print_entries_sorted(season.get_penalty_minutes_per_player())
    print '\n------------------\n'
    print 'Players and appearances:'
    print print_entries_sorted(season.get_players_and_number_of_matches_played())


def print_entries_sorted(match_events):
    s = ""
    for key, value in sorted(match_events.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        s += '\n' + key + ": " + str(value)
    print s
