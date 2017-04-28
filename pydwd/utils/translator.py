# -*- coding: utf-8 -*-

import os
import ConfigParser

import logger

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
configParser = ConfigParser.RawConfigParser()
configFilePath = os.path.join(folder_path, r'language.cfg')
configParser.read(configFilePath)


def translate_list(item_list):
    for index, item in enumerate(item_list):
        if not isinstance(item, list):
            try:
                item_list[index] = configParser.get('en', item.lower())
            except ConfigParser.NoOptionError, e:
                item_list[index] = item
                logger.warning('%s\nNo translation for value: %s' % (e, item))
        else:
            translate_list(item)
    return item_list
