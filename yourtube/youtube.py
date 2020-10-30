from pprint import pprint
import pyyoutube

from yourtube.config import config

# Initialize the api once during the loading phase of the program
# Just use it by importing `api` anywhere in this program
api = pyyoutube.Api(api_key=config["youtube"]["api_key"])


def get_videos_of_subscription(name):
    """Return all videos of a specific subscription."""
    # Get general information of this channel
    channels = api.get_channel_info(channel_name=name)
    channel = channels.items[0]

    # Looks like one has to look at the related playlists to get to the channel's uploads
    playlist_id = channel.contentDetails.relatedPlaylists.uploads

    all_uploads = []
    result = None
    while result is None or len(result.items) > 0:
        print("Playlist by id")
        result = api.get_playlist_by_id(playlist_id=playlist_id)
        pprint(playlist_id)
        pprint(result)
        pprint(result.items)
        all_uploads += result.items

        print("Playlist items")
        result = api.get_playlist_items(playlist_id=playlist_id, limit=50)
        pprint(result)
        pprint(result.items)
        all_uploads += result.items

    pprint(all_uploads)
