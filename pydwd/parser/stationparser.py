# -*- coding: utf-8 -*-

import re

from pydwd.utils import translator


def parse(file_content):
    result = {}

    if not file_content:
        return result

    keys = re.sub('\s{2,}', ' ', file_content[0]).strip()
    keys = re.sub('\s', ';', keys).split(';')
    keys = translator.translate_list(keys, translation='en-station')
    _line = re.sub('\s{2,}', ' ', file_content[1]).split()

    # convert date from YYYYMMDD to YYYY-MM-DD
    _line[1] = _line[1][:4] + '-' + _line[1][4:6] + '-' + _line[1][6:]
    _line[2] = _line[2][:4] + '-' + _line[2][4:6] + '-' + _line[2][6:]

    _line = __prepare_station_region_entries_(_line)

    for i in range(0, len(keys)):
        result.update({keys[i]: _line[i]})
    return result


def __prepare_station_region_entries_(_line):
    if len(_line) > 7:  # some station names consists of 2 or more words
        station_name = ''
        for i in range(6, len(_line) - 1):
            # concatenate every word on line between position 6 and n - 1,
            # where n is the last word and represents the region
            station_name = station_name + ' ' + _line[i]
        # correct station name remove white space at index 0
        _line[6] = station_name[1:]
        # and set last entry as region
        _line[7] = _line[len(_line) - 1]
    return _line


def get_by_index(file_content, index):
    result = []
    for line in file_content[2:]:
        _line = __prepare_station_region_entries_(re.sub('\s{2,}', ' ', line).split())
        if _line[index] not in result:
            result.append(_line[index])
    return result


def stations_by_value(file_content, value, index):
    result = []
    keys_line = file_content[0]
    for line in file_content[2:-1]:
        _line = re.sub('\s{2,}', ' ', line).split()
        if value in _line[index]:
            _station = parse([keys_line, line])
            result.append(_station)
    return result
