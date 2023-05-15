# -*- coding: utf-8 -*-

import os
import configparser
from configparser import RawConfigParser, NoOptionError

from . import logger

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
configparser = configparser.RawConfigParser()
configFilePath = os.path.join(folder_path, r'parameter.cfg')
configparser.read(configFilePath)


def translate_list(item_list, translation):
    for index, item in enumerate(item_list):
        if not isinstance(item, list):
            try:
                item_list[index] = configparser.get(translation, item)
            except NoOptionError as e:
                item_list[index] = item
                logger.warning('%s\nNo translation for value: %s' % (e, item))
        else:
            translate_list(item)
    return item_list

