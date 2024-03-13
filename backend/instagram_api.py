import requests
import urllib.parse


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
