PyDWD
=====

IN WORK

PyDWD crawl weather data from german weather stations. The weather data
are provided by [Deutscher Wetterdienst](http://www.dwd.de/).

How to use
----------

Example:

```python
   from pydwd.crawler.dailycrawler import DailyCrawler
   crawler = DailyCrawler()
   print crawler.by_city('Berlin-Tegel')
```

Output:

```bash
{'observation': 
    {'weather': 
        {'daily_snow_depth_(cm)': '0', 
        'daily_sunshine_duration_(h)': '1.567', 
        'precipitation_form': '6', 
        'daily mean of wind velocity_(m/s)': '6.2', 
        'daily_precipitation_height_(mm)': '3.5', 
        'daily_maximum_of_temperature_at_2m_height_(C)': '12.2', 
        'station_id': '430', 
        'daily_mean_of_temperature_(C)': '8.3', 
        'daily_mean_of_vapor_pressure_(hPa)': '7.6', 
        'daily_maximum_of_wind_gust_(m/s)': '16.8', 
        'date': '2018-01-01', 
        'quality_level_of_next_columns': '1', 
        'daily_mean_of_relative_humidity(%)': '69.08', 
        'daily_mean_of_pressure_(hPa)': '996.15', 
        'daily_minimum_of_temperature_at_2m_height_(C)': '4.1', 
        'daily_mean_of_cloud_cover_(1/8)': '6.1'
        }, 
    'station': 
        {'station_name': u'Berlin-Tegel', 
        'station_height': u'36', 
        'longitude': u'13.3088', 
        'latitude': u'52.5644', 
        'federal_state': u'Berlin', 
        'till_time': u'2018-01-01', 
        'from_time': u'1963-01-01', 
        'station_id': u'00430'
        }
    }
}
```

Functions:

* by_city('city name')
* by_region('region name')
* get_all_stations()
* get_all_regions()

How to install
--------------

```bash
$ git clone https://github.com/ckaus/pydwd.git
$ cd pydwd
$ sudo pip install .
```

License
-------

[MIT](https://github.com/ckaus/pydwd/blob/master/LICENSE) license
