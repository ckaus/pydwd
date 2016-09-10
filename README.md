PyDWD
=====

PyDWD crawl weather data from german weather stations. The weather data
are provided by [Deutscher Wetterdienst](http://www.dwd.de/).

How to use
----------

Example:

```python
   from pydwd.crawler.dailycrawler import DailyCrawler
   crawler = DailyCrawler()
   print crawler.by_city('Berlin-Buch')
```

Output:

```bash
{'observation':
    {'weather':
        {'wind_speed': '-999',
        'sunshine_duration': '-999', 
        'air_pressure_at_station': '-999', 
        'precipitation_height': '0.0', 
        'precipitation_height_ind': '0', 
        'min_soil_air_temperature': '11.9', 
        'measurement_date': '2016-09-08', 
        'relative_humidity': '70.17', 
        'air_temperature': '20.9', 
        'quality_level': '1', 
        'cloud_coverage': '-999', 
        'max_air_temperature': '29.3', 
        'min_air_temperature': '14.6', 
        'vapour_pressure': '16.4', 
        'id': '400', 
        'max_wind_speed': '-999'
        }, 
    'station':
        {'from_date': u'1961-01-01', 
        'station_height': u'60', 
        'till_date': u'2016-09-08', 
        'latitude': u'52.6309', 
        'federal_state': u'Berlin', 
        'station_name': u'Berlin-Buch', 
        'id': u'400', 
        'longitude': u'13.5022'
        }
    }
}
```

Features
--------

* Hourly weather data
* Daily weather data
* Monthly weather data


How to install
--------------

```bash
$ git clone https://github.com/ckaus/pydwd.git
$ cd pydwd && sudo pip install .
```

or

```bash
$ sudo pip install pydwd
```

Build from sources

```bash
$ git clone https://github.com/ckaus/pydwd.git
$ cd pydwd && python setup.py --command-packages=stdeb.command bdist_deb
$ cd deb_dist && sudo apt-get install python-pydwd_1.0.0-1_all.deb
```

License
-------

[MIT](https://github.com/ckaus/pydwd/blob/master/LICENSE) license