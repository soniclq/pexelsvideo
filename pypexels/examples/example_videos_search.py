###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_video_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 May 2020
#   Purpose: Exemplify usage of Video Search
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import logging
import os
import time
from datetime import datetime

from pypexels import PyPexels
import json

from pypexels.examples import videodown

api_key = os.environ.get('API_KEY', None) or 'DUMMY_API_KEY'


# Initialize app logging
logger = logging.getLogger()
logging.basicConfig(filename='app_video_search.log', level=logging.DEBUG)

# pypexels logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyPexels.logger_name).setLevel(logging.DEBUG)

# add a headers to the log
logger.debug(80*'=')
logging.debug('Testing PyPexels.videos_search()')
logger.debug(80*'=')
video_file= "/home/sonic/workplace/testvideo/pexels/"
# instantiate PyPexels object
def getTimeStr():
    return datetime.now().strftime("%m%d%H%M%S")
py_pexel = PyPexels(api_key=api_key)

# Start with the generic collection, maximize number of items per page
# Note: this will run until all popular photos have been visited,
#       unless a connection error occurs.
#       Typically the API hourly limit gets hit during this
#
#  Note2: the video API is not currently (May 2020) producing next_page/prev_page links
#         so this example will not be able to keep walking forward
#

def search_and_download(words):
    down_path = video_file + words
    folder = os.path.exists(down_path)
    if not folder:
        os.mkdir(down_path)
    else:
        pass
    count = 0
    while True:
        try:
            search_videos_page = py_pexel.videos_search(query=words, per_page=40)
            break;
        except Exception as e:
            print("!!!!!!!!!!!!" + e)
            pass

    # while True:
    for video in search_videos_page.entries:
        # print(video.id, video.user.get('name'), video.url)
        v_list = video.video_files
        for v in v_list:
            json_str = json.dumps(v)
            json_obj = json.loads(json_str)
            width = json_obj['width']
            height = json_obj['height']
            link = json_obj['link']
            if (height == 1080 and width == 1920):
                print(repr(width) + repr(height))
                try:
                    videodown.download_file(link, down_path + "/" + getTimeStr() + ".mp4")
                    print(link)
                except Exception as e:
                    print("!!!!!!!!!!!!!" + e)
                    pass
        time.sleep(15)
        count = count + 1
        if count > 20:
            break;
        # if not search_videos_page.has_next:
        #     break
        # count = count +1
        # if count >= 20:
        #     break;
        # search_videos_page = search_videos_page.get_next_page()

# download_list = ["river"]

# search_and_download("river")
# search_and_download("sea")
# search_and_download("mountain")
# search_and_download("sea wave")
# search_and_download("road")
# search_and_download("forest")
# search_and_download("rain")
# search_and_download("winter")
# search_and_download("summer")
# search_and_download("spring")
# search_and_download("autumn")
# search_and_download("bridge")
# search_and_download("garden")
# search_and_download("universe")
# search_and_download("stars")
# search_and_download("sunset")
# search_and_download("clouds")
# search_and_download("nature wallpaper")
search_and_download("sky")
search_and_download("Night Sky")