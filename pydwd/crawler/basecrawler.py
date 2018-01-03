# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
import codecs
import os.path

from pydwd.utils import ftphelper, logger
from pydwd.parser import stationparser


class BaseCrawler:
    def __init__(self):
        __metaclass__ = ABCMeta
        self.stations = self.__get_stations__()

    @abstractmethod
    def __get_weather__(self, id):
        pass

    def get_all_stations(self):
        return stationparser.get_by_index(self.stations, 6)

    def get_all_regions(self):
        return stationparser.get_by_index(self.stations, 7)

    def by_city(self, name):
        """
        Crawl weather data of a city by city name.

        :param name: City name
        :type name: str
        :returns: Observations as dict
        """
        station_list = stationparser.stations_by_value(self.stations, name, 6)

        if len(station_list) == 0:
            return {}

        tmp_station_list = station_list
        idx = 0
        for station in station_list:
            station_name = station['station_name']
            if len(name) < len(station_name) \
                    and station_name[len(name)] is not '-':
                        print "DEL %s" % (station_name)
                        del tmp_station_list[idx]

            idx += 1
        if len(tmp_station_list) > 1:
            return self.__build_observation_list__(tmp_station_list)
        return self.__build_observation__(tmp_station_list[0])

    def by_region(self, name):
        """
        Crawl weather data of a region by region (state) name.
        :param name: Region name
        :returns: Observations as dict.
        """
        station_list = stationparser.stations_by_value(self.stations, name, 7)
        return self.__build_observation_list__(station_list)

    def __get_stations__(self):
        # Check whether locally station description file exist
        if not os.path.isfile(self._station_file):
            # download station description file from ftp server
            logger.warning('File: %s not exist locally.' % self._station_file)
            ftphelper.download_file(self._host, self._data_path, self._station_file)

        local_file_time = int(os.path.getmtime(self._station_file))
        remote_file_time = ftphelper.get_modified_time_of_file(self._host,
                                                               self._data_path,
                                                               self._station_file)

        # compare time since epoch
        if local_file_time < remote_file_time:
            # remote file is newer ( time stamp is higher )
            logger.info('Remote file is newer')
            ftphelper.download_file(self._host, self._data_path, self._station_file)

        try:
            with codecs.open(self._station_file, 'r', encoding='ISO-8859-1') as f:
                return f.readlines()
        except IOError, error:
            logger.error('Cannot open local file: %s.' % (error, self._station_file))
            return None

    def __build_observation_list__(self, station_list):
        result = {'observation-list': []}
        for station in station_list:
            observation = self.__build_observation__(station)
            if observation:  # station is active
                result['observation-list'].append(observation)
        return result

    def __build_observation__(self, station):
        weather = self.__get_weather__(station['station_id'])
        result = {'observation': {}}
        result['observation']['station'] = station
        result['observation']['weather'] = weather
        return result
