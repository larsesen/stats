#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from enum import Enum


class MatchResult(Enum):
    WIN = 'Victory',
    WIN_PEN = 'Victory pen',
    LOSS_PEN = 'Loss pen'
    LOSS = 'Loss'


class Teams(Enum):
    LYN = 'Lyn'
    BMIL = 'BMIL',
    UllKisa = 'Ull/Kisa',
    Grei = 'Grei',
    Lillestrom = 'Lillestrøm',
    Ajer = 'Ajer',
    Oreasen = 'Øreåsen',
    Valerenga = 'Vålerenga'


map_team_name_to_shortname = {u'Lyn Innebandy': 'Lyn',
                              u'BMIL Herrer 1': 'BMIL',
                              u'Ullensaker/Kisa IL': 'Ull/Kisa',
                              u'Grei': 'Grei',
                              u'Lillestrøm Innebandyklubb': 'Lillestrøm',
                              u'Ajer': 'Ajer',
                              u'Øreåsen': 'Øreåsen',
                              u'Vålerenga': 'Vålerenga'}
