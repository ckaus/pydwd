# -*- coding: utf-8 -*-

from pydwd.crawler.basecrawler import BaseCrawler
from pydwd.utils import ftphelper, translator
from pydwd.parser import weatherparser


class HourlyCrawler(BaseCrawler):
    def __init__(self):
        self._host = 'opendata.dwd.de'
        self._data_path = '/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/'
        self._station_file = 'TU_Stundenwerte_Beschreibung_Stationen.txt'
        BaseCrawler.__init__(self)

    def __get_weather__(self, id):
        url = 'ftp://' + self._host + self._data_path
        _id = '%05d' % int(id)

        # temperature file path
        temp_path = 'stundenwerte_TU_' + _id + '_akt.zip'
        # wind path file path
        #wind_path = '/wind/recent/stundenwerte_FF_' + _id + '_akt.zip'
        # cloudiness file path
        #clou_path = '/cloudiness/recent/stundenwerte_N_' + _id + '_akt.zip'
        # preciption file path
        #prec_path = '/precipitation/recent/stundenwerte_RR_' + _id + '_akt.zip'
        # pressure file path
        #pres_path = '/pressure/recent/stundenwerte_P0_' + _id + '_akt.zip'

        temp_file = 'produkt_tu_stunde_'
        #wind_file = 'produkt_ff_stunde_'
        #clou_file = 'produkt_n_stunde_'
        #prec_file = 'produkt_rr_stunde_'
        #pres_file = 'produkt_p0_stunde_'

        url_dict = {'temperature': [url + temp_path, temp_file],
                    #'wind': [url + wind_path, wind_file],
                    #'cloudiness': [url + clou_path, clou_file],
                    #'precipitation': [url + prec_path, prec_file],
                    #'pressure': [url + pres_path, pres_file]
                    }

        result = {}
        for key, value in url_dict.items():
            content = ftphelper.get_file_txt_zip(value[0], value[1])
            if content:
                result[key] = weatherparser.parse(content, translation='en-hourly')
            else:
                result[key] = {}
        return result
