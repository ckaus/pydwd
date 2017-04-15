# -*- coding: utf-8 -*-

from pydwd.crawler.basecrawler import BaseCrawler
from pydwd.utils import ftphelper
from pydwd.parser import weatherparser

class HourlyCrawler(BaseCrawler):
    def __init__(self):
        self._host = 'ftp-cdc.dwd.de'
        self._station_file = 'TU_Stundenwerte_Beschreibung_Stationen.txt'
        self._data_path = '/pub/CDC/observations_germany/climate/hourly/air_temperature/recent/'
        BaseCrawler.__init__(self)

    def __get_weather__(self, id):
        url = 'ftp://' + self._host + '/pub/CDC/observations_germany/climate/hourly'
        _id = '%05d' % int(id)

        # temperature file path
        temp_path = '/air_temperature/recent/stundenwerte_TU_' + _id + '_akt.zip'
        # wind path file path
        wind_path = '/wind/recent/stundenwerte_FF_' + _id + '_akt.zip'
        # cloudiness file path
        clou_path = '/cloudiness/recent/stundenwerte_N_' + _id + '_akt.zip'
        # preciption file path
        prec_path = '/precipitation/recent/stundenwerte_RR_' + _id + '_akt.zip'
        # pressure file path
        pres_path = '/pressure/recent/stundenwerte_P0_' + _id + '_akt.zip'

        temp_file = 'produkt_temp_Terminwerte_'
        wind_file = 'produkt_wind_Terminwerte_'
        # (c)loud, (p)reciption, (p)ressure
        c_p_p_file = 'produkt_synop_Terminwerte_'

        url_dict = {'temperature': [url + temp_path, temp_file],
                    'wind': [url + wind_path, wind_file],
                    'cloudiness': [url + clou_path, c_p_p_file],
                    'precipitation': [url + prec_path, c_p_p_file],
                    'pressure': [url + pres_path, c_p_p_file]}

        result = {}
        for key, value in url_dict.iteritems():
            content = ftphelper.get_file_txt_zip(value[0], value[1])
            if content:
                result[key] = weatherparser.parse(content)
            else:
                result[key] = {}
        return result
