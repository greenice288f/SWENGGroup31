import requests
import urllib.parse
import urllib.request
import os


_client_id = '427613722975596'
_client_secret = 'a7746d46ad0cc8572acb1757e50d169f'
# _redirect_endpoint = 'http://localhost:5000/api/instagram-redirect'
_redirect_endpoint = 'https://trinity.richardblazek.com/api/instagram-redirect'

REDIRECT_URL = 'https://api.instagram.com/oauth/authorize' \
            + f'?client_id={_client_id}' \
            + f'&redirect_uri={urllib.parse.quote(_redirect_endpoint)}' \
            + f'&scope=user_profile,user_media&response_type=code'

def get_credentials(code: str) -> tuple[str, str]:
    result = requests.post('https://api.instagram.com/oauth/access_token', data = {
        'client_id': _client_id,
        'client_secret': _client_secret,
        'redirect_uri': _redirect_endpoint,
        'code': code,
        'grant_type': 'authorization_code'
    }).json()
    return str(result['user_id']), result['access_token']

def _get_media_by_id(media_id, access_token) -> tuple[list[tuple[str, str]], str]:
    media = requests.get(f'https://graph.instagram.com/v19.0/{media_id}?fields=id,media_type,caption,media_url&access_token={access_token}').json()
    caption = media.get('caption') or ''

    if media['media_type'] in {'IMAGE', 'VIDEO'}:
        return [(media['media_url'], media['media_type'])], caption

    children = requests.get(f'https://graph.instagram.com/v19.0/{media_id}/children?fields=id,media_type,media_url&access_token={access_token}').json()
    return [(child['media_url'], media['media_type']) for child in children['data']], caption

def get_media(user_id, access_token) -> tuple[list[tuple[str, str]], list[str]]:
    result = requests.get(f'https://graph.instagram.com/v19.0/{user_id}?fields=id,username,media&access_token={access_token}').json()
    media_ids = [m['id'] for m in result['media']['data']]
    media = [_get_media_by_id(media_id, access_token) for media_id in media_ids]
    comments = [comment for _, comment in media]
    assets = [asset for lst, _ in media for asset in lst]
    return assets, comments

def download_images(assets, directory):
    os.makedirs(directory, exist_ok=True)
    for i, (media_url, media_type) in enumerate(assets):
        if media_type == 'IMAGE':
            urllib.request.urlretrieve(media_url, os.path.join(directory, f'img{i}.jpg'))
