from datetime import datetime, timedelta
import json
import requests

# Load the configuration containing the required facebook information
with open("config.json", "r") as config_file:
    fb_config = json.load(config_file)

access_token = fb_config['access_token']
app_id = fb_config['id']

base_url = "https://graph.facebook.com/{}/feed?access_token={}".format(app_id, access_token)
headers = {'content-type': 'application/json'}


def publish_burger_in_future(burger, days=1):
    """
    Schedule posts a burger to Facebook unpublished

    :param burger: Burger to post
    :param days: Days in the future to post the burger
    :return: Response from Facebook
    """
    now = datetime.now() + timedelta(days=days)
    timestamp = int(datetime.timestamp(now))

    # Build URL and output it for verification
    post_url = base_url + "&message={}&scheduled_publish_time={}&published=false".format(burger, timestamp)
    print(post_url)
    response = requests.post(post_url, headers=headers)

    return response
