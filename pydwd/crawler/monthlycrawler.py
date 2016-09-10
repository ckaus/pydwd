# -*- coding: utf-8 -*-

from .basecrawler import BaseCrawler
from ..parser import weatherparser
from ..utils import ftphelper


class MonthlyCrawler(BaseCrawler):
    def __init__(self):
        self._host = 'ftp.dwd.de'
        self._data_path = '/pub/CDC/observations_germany/climate/monthly/kl/recent/'
        self._station_file = 'KL_Monatswerte_Beschreibung_Stationen.txt'
        BaseCrawler.__init__(self)

    def __get_weather__(self, id):
        file_name = 'produkt_monat_Monatswerte_'
        archive_name = 'monatswerte_' + '%05d' % int(id) + '_akt.zip'
        file_url = 'ftp://' + self._host + self._data_path + archive_name
        content = ftphelper.get_file_txt_zip(file_url, file_name)
        return weatherparser.parse(content)
