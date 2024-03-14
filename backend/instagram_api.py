import requests
import urllib.parse
import urllib.request
import os

_client_id = '427613722975596'
_client_secret = 'a7746d46ad0cc8572acb1757e50d169f'

def get_credentials(code: str, host: str) -> tuple[str, str]:
    origin = 'http://localhost:5000' if 'localhost' in host else 'https://trinity.richardblazek.com'
    result = requests.post('https://api.instagram.com/oauth/access_token', data = {
        'client_id': _client_id,
        'client_secret': _client_secret,
        'redirect_uri': f'{origin}/api/instagram-redirect',
        'code': code,
        'grant_type': 'authorization_code'
    }).json()
    return str(result['user_id']), result['access_token']

def _get_media_by_id(media_id: str, access_token: str) -> list[tuple[str, str, str]]:
    media = requests.get(f'https://graph.instagram.com/v19.0/{media_id}?fields=media_type,caption,media_url&access_token={access_token}').json()
    caption = media.get('caption') or ''

    if media['media_type'] in {'IMAGE', 'VIDEO'}:
        return [(media['media_url'], media['media_type'], caption)]

    children = requests.get(f'https://graph.instagram.com/v19.0/{media_id}/children?fields=media_type,media_url&access_token={access_token}').json()
    return [(child['media_url'], media['media_type'], caption) for child in children['data']]

def _get_media(user_id: str, access_token: str) -> list[tuple[str, str, str]]:
    result = requests.get(f'https://graph.instagram.com/v19.0/{user_id}?fields=media&access_token={access_token}').json()
    ids = [str(m['id']) for m in result['media']['data']]
    return [media for media_id in ids for media in _get_media_by_id(media_id, access_token)]

def _save_media_to(media: list[tuple[str, str, str]], directory: str):
    os.makedirs(directory, exist_ok=True)
    for i, (media_url, media_type, comment) in enumerate(media):
        if media_type == 'IMAGE':
            urllib.request.urlretrieve(media_url, os.path.join(directory, f'post{i}.jpg'))
            with open(os.path.join(directory, f'post{i}.txt'), mode='w') as comment_file:
                comment_file.write(comment)

def download_media(user_id: str, access_token: str, directory: str):
    media = _get_media(user_id, access_token)
    _save_media_to(media, directory)
