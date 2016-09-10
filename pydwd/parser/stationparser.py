# -*- coding: utf-8 -*-

import re

from ..utils import translator


def parse(file_content):
    result = {}

    if not file_content:
        return result

    keys = re.sub('\s{2,}', ' ', file_content[0]).strip()
    keys = re.sub('\s', ';', keys).split(';')
    keys = translator.translate_list(keys)
    _line = re.sub('\s{2,}', ' ', file_content[1]).split()

    # convert date from YYYYMMDD to YYYY-MM-DD
    _line[1] = _line[1][:4] + '-' + _line[1][4:6] + '-' + _line[1][6:]
    _line[2] = _line[2][:4] + '-' + _line[2][4:6] + '-' + _line[2][6:]

    if len(_line) > 7:  # some station names consists of 2 or more words
        station_name = ''
        for i in range(6, len(_line) - 1):
            # concatenate every word on line between position 6 and n - 1,
            # where n is the last word and represents the region
            station_name = station_name + ' ' + _line[i]
        # replace station name remove white space at index 0
        _line[6] = station_name[1:]
        # set last entry as region
        _line[7] = _line[len(_line) - 1]
    for i in range(0, len(keys)):
        result.update({keys[i]: _line[i]})
    return result


def stations_by_value(file_content, value, index):
    result = []
    keys_line = file_content[0]
    for line in file_content[3:-1]:
        _line = re.sub('\s{2,}', ' ', line).split()
        if value in _line[index]:
            # extract line with given id and keys and create new file_content
            _station = parse([keys_line, line])
            result.append(_station)
    return result
