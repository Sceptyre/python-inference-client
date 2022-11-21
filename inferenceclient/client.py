import hashlib
from requests.sessions import session
from . import api

class InferenceClient(object):
    _username = None
    _password = None
    _apikey = None
    _token = None
    session = None

    def _digest_response(self) -> str:
        # Generate md5 response
        ha1 = hashlib.md5(
            bytes(f'{self._username}:Please enter your email and secret_key.:{self._password}', 'ascii')
        )
        ha2 = hashlib.md5(
            b'POST:/studio_instance/studio-api/v1/auth/get-token/'
        )
        response = hashlib.md5(
            bytes(ha1.hexdigest() + ":12345:1:12345:auth:" + ha2.hexdigest(), 'ascii')
        )

        # Return formatted auth header
        return f'''Digest username="{self._username}", realm="Please enter your email and secret_key.", nonce="12345", uri="/studio_instance/studio-api/v1/auth/get-token/", algorithm="MD5", qop=auth, nc=1, cnonce="12345", response="{response.hexdigest()}"'''

    def _get_token(self) -> str:
        r = self.session.post(
            'https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/auth/get-token/',
            data={
                'apikey':self._apikey
            }
        )
        r.raise_for_status()

        return r.json()['result']['token']

    def _query(self, path: str, params: dict = {}) -> dict:
        r = self.session.post(
            url=path,
            data={
                'token': self._token,
                **params
            }
        )
        r.raise_for_status()

        return r.json()['result']

    def __init__(self, username: str, secret: str, apikey: str, verify_ssl=True) -> None:
        # Store params
        self._username = username
        self._password = secret
        self._apikey = apikey

        # Build session
        self.session = session()
        self.session.verify = verify_ssl
        self.session.headers["Authorization"] = self._digest_response()
        
        # Get token
        self._token = self._get_token()

        # Map methods
        self.datastores = api.DatastoresAPI(self)