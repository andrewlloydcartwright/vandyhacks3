import pycurl
from io import BytesIO
import os
# import json
# import time
# import numpy

# Sample HTTP request from NASA 
    # https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=NASA_api_key

# Sample request from asterank 
    # http://asterank.com/api/asterank?query={query}&limit={limit}
    #  /api/asterank?query={"e":{"$lt":0.1},"i":{"$lt":4},"a":{"$lt":1.5}}&limit=1  

def get_NASA_data():
    NASA_api_key = 'kRRhklDl87rpJP5YRhJSmtQALYt3HjKgo6fvUw0H'
    c = pycurl.Curl()
    f = open('NASA_data.json', 'a+')
    f.write('[')

    # This API only supports requests of date ranges spanning one week.
    # Requests are limited to 1,000 total per hour. 
    NASA_api_requests = [
        ############    October
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-10-01&end_date=2016-10-07&api_key=' + NASA_api_key,
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-10-08&end_date=2016-10-14&api_key=' + NASA_api_key,
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-10-15&end_date=2016-10-21&api_key=' + NASA_api_key,
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-10-22&end_date=2016-10-28&api_key=' + NASA_api_key,
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-10-29&end_date=2016-10-31&api_key=' + NASA_api_key,
        ############    November to date
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-11-01&end_date=2016-11-07&api_key=' + NASA_api_key,
        'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-11-08&end_date=2016-11-12&api_key=' + NASA_api_key
    ]

    for item in NASA_api_requests:
        buffer = BytesIO()
        c.setopt(c.URL, item)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        body = buffer.getvalue()
        f.write(body)
        f.write(',')

    f.seek(0, os.SEEK_END)
    pos = f.tell() - 1
    f.truncate
    f.write(']')
    f.close
    c.close


def get_asterrank_data():
    buffer = BytesIO()
    c = pycurl.Curl()
    f = open('asterrank_data.json', 'a+')
    c.setopt(c.URL, 'http://www.asterank.com/api/asterank?query={"price":{"$gt":1000000,"$lt":50000000000}}&limit=10')
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    body = buffer.getvalue()
    f.write(body)
    f.close
    c.close


get_NASA_data()
get_asterrank_data()

# json_string = f.read()
# json_data = json.loads(json_string)


# # NASA_dict = {'asteroid_id': 'name', 'close_call_date': 'YYYY-MM-DD', 'close_call_distance': 'miles away', 'close_call_velocity': 'relative speed'}
# # asterank_dict = {}

# # for item in f:
# #     NASA_dict['asteroid_id']=item.get(name)
# #     NASA_dict['close_call_date']=item.get(close_approach_data).get(close_approach_date)
# #     NASA_dict['close_call_distance']=item.get(close_approach_dat_data).get(miles)
# #     NASA_dict['close_call_velocity']=item.get(close_approach_data).get(relative_velocity).get(miles_per_hour)
# #     result.append(NASA_dict)
# #     print NASA_dict

# # print NASA_dict

