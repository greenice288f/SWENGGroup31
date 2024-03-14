import requests
import urllib.parse
import urllib.request
import os
import shutil


# Client ID and client secret for the Instagram API
_client_id = '427613722975596'
_client_secret = 'a7746d46ad0cc8572acb1757e50d169f'


# Obtains the user id and the access token from Instagram.
# Arguments:
#   - code: the authentication code we got from Instagram
#   - host: the host header (to know if we're running on localhost or on the server)
# Return value:
#   - a tuple of two strings:
#       1. the user id
#       2. the access token
def get_credentials(code: str, host: str) -> tuple[str, str]:
    origin = 'https://trinity.richardblazek.com' if 'trinity' in host else 'http://localhost:5000'
    result = requests.post('https://api.instagram.com/oauth/access_token', data = {
        'client_id': _client_id,
        'client_secret': _client_secret,
        'redirect_uri': f'{origin}/api/instagram-redirect',
        'code': code,
        'grant_type': 'authorization_code'
    }).json()
    return str(result['user_id']), result['access_token']


# Fetches data about the specified media
# Arguments:
#   - media_id: the id of the media we're interested in
#   - access_token: the access token (returned from get_credentials)
# Return value:
#   - a list of tuples of three strings:
#       1. the url of the given image or video file
#       2. the media type (IMAGE or VIDEO)
#       3. the comment of the post's author
def _get_media_by_id(media_id: str, access_token: str) -> list[tuple[str, str, str]]:
    media = requests.get(f'https://graph.instagram.com/v19.0/{media_id}?fields=media_type,caption,media_url&access_token={access_token}').json()
    caption = media.get('caption') or ''

    if media['media_type'] in {'IMAGE', 'VIDEO'}:
        return [(media['media_url'], media['media_type'], caption)]

    children = requests.get(f'https://graph.instagram.com/v19.0/{media_id}/children?fields=media_type,media_url&access_token={access_token}').json()
    return [(child['media_url'], media['media_type'], caption) for child in children['data']]


# Fetches data about all media of the given user
# Arguments:
#   - user_id: the id of the user whose media we're interested in
#   - access_token: the access token (returned from get_credentials)
# Return value:
#   - a list of tuples of three strings:
#       1. the url of the given image or video file
#       2. the media type (IMAGE or VIDEO)
#       3. the comment of the post's author
def _get_media(user_id: str, access_token: str) -> list[tuple[str, str, str]]:
    result = requests.get(f'https://graph.instagram.com/v19.0/{user_id}?fields=media&access_token={access_token}').json()
    ids = [str(m['id']) for m in result['media']['data']]
    return [media for media_id in ids for media in _get_media_by_id(media_id, access_token)]


# Saves all images and comments to the given directory
# Arguments:
#   - media: a list of tuples of urls, media types and comments
#   - directory: the destination directory where we want to save files
# Return value: None
def _save_media_to(media: list[tuple[str, str, str]], directory: str):
    shutil.rmtree(directory, ignore_errors=True)
    os.makedirs(directory, exist_ok=True)
    for i, (media_url, media_type, comment) in enumerate(media):
        if media_type == 'IMAGE':
            urllib.request.urlretrieve(media_url, os.path.join(directory, f'post{i}.jpg'))
            with open(os.path.join(directory, f'post{i}.txt'), mode='w') as comment_file:
                comment_file.write(comment)


# Downloads all media of the given user to the given directory.
# Arguments:
#   - user_id: the id of the user whose media we're interested in
#   - access_token: the access token (returned from get_credentials)
#   - directory: the destination directory where we want to save files
def download_media(user_id: str, access_token: str, directory: str):
    _save_media_to(_get_media(user_id, access_token), directory)
