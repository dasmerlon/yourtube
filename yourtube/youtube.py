from pprint import pprint
from googleapiclient.discovery import build

from yourtube.config import config

# Initialize the api once during the loading phase of the program
# Just use it by importing `api` anywhere in this program
# Check google's official python api docs for more info:
# https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md
# https://github.com/googleapis/google-api-python-client/blob/master/docs/api-keys.md
#
# Google's official api docs also have an api-tester on the right side of the screen
# This can be also used to show code examples by clicking on `Show Code`.
# There are python code examples for pretty much everything.
# For example:
# https://developers.google.com/youtube/v3/docs/channels/list
# https://developers.google.com/youtube/v3/docs/playlists/list
# https://developers.google.com/youtube/v3/docs/playlistItems/list
youtube = build("youtube", "v3", developerKey=config["youtube"]["api_key"])


def get_channel_videos(channel_name):
    channel_response = (
        youtube.channels()
        .list(part="contentDetails,topicDetails", id="UCZNTsLA6t6bRoj-5QRmqt_w")
        .execute()
    )
    # Get the first item (only one should exist at a time
    channel = channel_response["items"][0]

    # Get the playlist id of the channel's uploads
    playlist_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    pprint(playlist_id)

    # Query playlist items
    playlist_response = (
        youtube.playlistItems()
        .list(part="contentDetails", playlistId=playlist_id)
        .execute()
    )

    pprint(playlist_response)
    return playlist_response
