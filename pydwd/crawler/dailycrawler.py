# -*- coding: utf-8 -*-

from pydwd.crawler.basecrawler import BaseCrawler
from pydwd.utils import ftphelper, translator
from pydwd.parser import weatherparser


class DailyCrawler(BaseCrawler):
    def __init__(self):
        self._host = 'opendata.dwd.de'
        self._data_path = '/climate_environment/CDC/observations_germany/climate/daily/kl/recent/'
        self._station_file = 'KL_Tageswerte_Beschreibung_Stationen.txt'
        BaseCrawler.__init__(self)

    def __get_weather__(self, id):
        file_name = 'produkt_klima_'
        archive_name = 'tageswerte_KL_' + '%05d' % int(id) + '_akt.zip'
        file_url = 'ftp://' + self._host + self._data_path + archive_name
        content = ftphelper.get_file_txt_zip(file_url, file_name)
        return weatherparser.parse(content, translation='en-daily')
