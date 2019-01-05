#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Insert new id's to get data from match.

import json
from bs4 import BeautifulSoup
import requests


base_url = "https://wp.nif.no/PageMatchWithResult.aspx?LinkId="
match_ids = ['6861083','6861084','6861085','6861086','6861087','6861088','6861089','6861090','6861091','6861092',
            '6861093','6861094','6861095','6861096','6861097','6861098','6861099','6861100','6861101','6861102',
            '6861103','6861104','6861105','6861106','6861107','6861108','6861109','6861110','6861111','6861112',
            '6861113','6861114','6861115','6861116','6861117','6861118','6861119','6861120','6861121','6861122',
            '6861123','6861124','6861125','6861126','6861127','6861129','6861130','6861156']

for match_id in match_ids:

    request = requests.get(base_url + match_id)
    soup = BeautifulSoup(request.text, 'html.parser')

    match_data = soup.findAll('script')[26]
    team_vm = '{' + '\"participants\": [' + match_data.text.split('var teamVM = ')[1].split(',\"BindingContainerId')[0] + '}]'
    info = '\"info\": [' + match_data.text.split('var matchBasicInfoVM = ')[1].split('\n')[0][:-2] + ']'
    goals = '\"goals\": [' + match_data.text.split('var goalsInOrderVM = ')[1].split('\n')[0][:-2] + ']'
    pens = '\"pens\": [' + match_data.text.split('var matchPenaltiesVM = ')[1].split('\n')[0][:-2] + ']'

    text_string = team_vm + ',' + info + ',' + goals + ',' + pens + '}'
    json_string = json.loads(text_string)

    timestamp = json_string['info'][0]['MatchDate'][:10]
    home = json_string['info'][0]['HomeTeamName'][:3]
    away = json_string['info'][0]['AwayTeamName'][:3]

    file_name = 'match_reports/' + timestamp + '_' + home + '_' + away + '.json'
    with open(file_name, 'w') as file:
        file.write(json.dumps(json_string, ensure_ascii=False).encode('utf-8'))
