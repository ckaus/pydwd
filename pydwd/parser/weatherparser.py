# -*- coding: utf-8 -*-

import re

from pydwd.utils import translator


def parse(file_content, translation):
    result = {}

    if not file_content:
        return result

    keys = re.sub('\s+', ' ', file_content[0])
    keys = re.sub('(;\s)', ';', keys)
    keys = keys.strip().split(';')
    keys.pop()  # remove last entry: eor
    keys = translator.translate_list(keys, translation)
    last_entry_line = len(file_content) - 2  # get line of last entry
    values = re.sub('(\s|\t)+', '', file_content[last_entry_line])
    values = values.strip().split(';')

    if len(values[1]) > 8:
        # convert date from YYYYMMDDHH to YYYY-MM-DD HH:MM:SS
        values[1] = values[1][:4] + '-' + values[1][4:6] + '-' + values[1][6:8] \
                    + ' ' + values[1][8:10] + ':00:00'
    else:
        # convert date from YYYYMMDD to YYYY-MM-DD
        values[1] = values[1][:4] + '-' + values[1][4:6] + '-' + values[1][6:8]

    for i in range(0, len(keys) - 1):  # without last entry: 'eor'
        result.update({keys[i]: values[i]})
    return result
