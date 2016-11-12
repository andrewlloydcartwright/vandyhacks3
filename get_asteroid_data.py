import pycurl
from io import BytesIO
import time
import numpy

NASA_api_key = 'kRRhklDl87rpJP5YRhJSmtQALYt3HjKgo6fvUw0H'


# Sample HTTP request from NASA 
    # https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=NASA_api_key

# Sample request from asterank 
    # http://asterank.com/api/asterank?query={query}&limit={limit}
    #  /api/asterank?query={"e":{"$lt":0.1},"i":{"$lt":4},"a":{"$lt":1.5}}&limit=1  
buffer = BytesIO()
asteroid_list = {}

c = pycurl.Curl()
c.setopt(c.URL, 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-11-05&end_date=2016-11-11&api_key=kRRhklDl87rpJP5YRhJSmtQALYt3HjKgo6fvUw0H')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close
body = buffer.getvalue()
f = open('data.json', 'a')
f.write(body)

# for item in body:
#     my_dict['asteroid_id']=item.get('name')
#     my_dict['close_call_date']=item.get('close_approach_data').get('close_approach_date')
#     my_dict['close_call_distance']=item.get('close_approach_dat_data').get('miles')
#     my_dict['close_call_velocity']=item.get('close_approach_data').get('relative_velocity').get('miles_per_hour')
#     result.append(my_dict)
