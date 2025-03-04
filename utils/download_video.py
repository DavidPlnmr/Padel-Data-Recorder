from pytube.download_helper import (
    download_video,
)
import sys

# Get the url as params args
url = sys.argv[1]


# This code creates an error but the video is actually downloaded without any problem
# download_video(url=url)

# We dodge the error because it makes no sense as it actually download
try:
    download_video(url=url)
except Exception as e:
    # print(e)
    pass

# Try something like this :
# python utils/download_video.py "https://www.youtube.com/watch?v=yaE2Yh5yxzk"