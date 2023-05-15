# -*- coding: utf-8 -*-

import datetime
import ftplib
import io
import time
import traceback
from urllib.request import urlopen
import zipfile
from urllib.request import HTTPError, URLError

from . import logger


def get_modified_time_of_file(host, file_path, file_name):
    modified_time = 0
    try:
        ftp = ftplib.FTP(host)
        ftp.login()
        ftp.cwd(file_path)
        modified_time = ftp.sendcmd('MDTM %s' % file_name)[4:]
        ftp.quit()

        year = int(modified_time[:4])
        month = int(modified_time[4:6])
        day = int(modified_time[6:8])
        hour = int(modified_time[8:10])
        minute = int(modified_time[10:12])
        seconds = int(modified_time[12:14])

        remote_file_time = datetime.datetime(year, month, day, hour, minute, seconds)
        modified_time = int(time.mktime(remote_file_time.timetuple()))
    except ftplib.all_errors as e:
        logger.warning('%s\nNot able to get date of remote description file. Check your connection' % e)
    return modified_time


def download_file(host, file_path, file_name):
    try:
        ftp = ftplib.FTP(host)
        ftp.login()
        ftp.cwd(file_path)
        ftp.retrbinary('RETR ' + file_path + file_name, open(file_name, 'wb').write)
        logger.success('Download: %s' % host + file_path + file_name)
        ftp.quit()
    except ftplib.all_errors as e:
        logger.error('%s\nCannot download file: %s.' % (e, host + file_path + file_name))


def get_file_txt_zip(url, file_name):
    file_socket = get_response(url)
    if file_socket is None:
        return None
    archive_bytes = io.BytesIO(file_socket.read())
    archive_file = zipfile.ZipFile(archive_bytes, 'r')
    for name in archive_file.namelist():
        if file_name in name:
            file_content = archive_file.open(name, 'r')
            archive_file.close()
            return [str(i,'utf-8') for i in file_content.readlines()]
    return None


def get_response(url):
    try:
        return urlopen(url)
    except (HTTPError, URLError):
        logger.warning('File: %s not found.' % url)
    except Exception as error:
        logger.error('Exception: %s' % (traceback.format_exc(), error))
    return None
