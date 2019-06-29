# -*- coding: utf-8 -*-
import time
from datetime import datetime


def datetime_to_str(datetime, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(format)


def utc_to_datetime(time_str):
    return datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')


def now_time():
    now = datetime.now()
    return now


def now_time_str():
    return datetime_to_str(now_time())


def str_to_datetime(str, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(str, format)


def utc_to_local(utc_st):
    '''UTC时间转本地时间（+8:00）'''
    now_stamp = time.time()
    local_time = datetime.fromtimestamp(now_stamp)
    utc_time = datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def local2utc(local_st):
    '''本地时间转UTC时间（-8:00）'''
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.utcfromtimestamp(time_struct)
    return utc_st


def time_loads(str):
    utc_st = utc_to_datetime(str)
    return utc_to_local(utc_st)
