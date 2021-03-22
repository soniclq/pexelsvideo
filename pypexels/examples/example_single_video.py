###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_popular.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 27 Sep 2017
#   Purpose: Exemplify usage of Popular
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import logging
import os
from pypexels import PyPexels
import json
import videodown
# api_key = os.environ.get('API_KEY', None) or 'DUMMY_API_KEY'
api_key = "563492ad6f91700001000001ba2c5c9bac0044a7bf3826f1939654fd"

# Initialize app logging
logger = logging.getLogger()
logging.basicConfig(filename='app_single_video.log', level=logging.DEBUG)

# pypexels logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PyPexels.single_video()')
logger.debug(80*'=')

# instantiate PyPexels object
py_pexel = PyPexels(api_key=api_key)

# Retrieve a single video, known by its ID
video = py_pexel.single_video(video_id=1448735)
print(video.id, video.user.get('name'), video.url)
print(video.get_attribution('txt'))
print(video.get_attribution('html'))
# print(video.video_files)
v_list = video.video_files
json_str = json.dumps(v_list[0])
json_obj = json.loads(json_str)
print(json_obj['file_type'])
count = 0
for v in v_list:
    json_str = json.dumps(v)
    json_obj = json.loads(json_str)
    width = json_obj['width']
    height = json_obj['height']
    link = json_obj['link']
    print(link)
    count += 1
    videodown.download_file(link, "//Users/momo/PycharmProjects/pypexels/"+repr(count)+".mp4")
    # if(height == 1080 and width == 1920):
    #     print(repr(width) + repr(height))
    #     print(link)
    # print(json_obj['height'])
# print(video.g)
