# -*- coding: utf-8 -*-

from pydwd.crawler.basecrawler import BaseCrawler
from pydwd.utils import ftphelper, translator
from pydwd.parser import weatherparser


class MonthlyCrawler(BaseCrawler):
    def __init__(self):
        self._host = 'ftp-cdc.dwd.de'
        self._data_path = '/pub/CDC/observations_germany/climate/monthly/kl/recent/'
        self._station_file = 'KL_Monatswerte_Beschreibung_Stationen.txt'
        BaseCrawler.__init__(self)

    def __get_weather__(self, id):
        file_name = 'produkt_klima_monat_'
        archive_name = 'monatswerte_KL_' + '%05d' % int(id) + '_akt.zip'
        file_url = 'ftp://' + self._host + self._data_path + archive_name
        content = ftphelper.get_file_txt_zip(file_url, file_name)
        return weatherparser.parse(content, translation='en-monthly')
