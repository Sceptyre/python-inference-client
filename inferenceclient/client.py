from requests.sessions import session, Session
from . import api

class InferenceClient(object):
    _apikey: str
    session: Session = session()
    base_url: str

    datastores: api.DatastoresAPI

    def __init__(self, apikey: str, account_id: str, region: str = 'us', scope: str = 'ac', verify_ssl=True) -> None:
        # Store params
        self._apikey = apikey
        self.base_url = f'https://api.{region.lower()}7.studioportal.io/api'

        # Build session
        self.session.verify = verify_ssl
        self.session.headers['studio-api-key'] = self._apikey
        self.session.headers['scope'] = scope
        self.session.headers['scope-id'] = account_id

        # Map methods
        self.datastores = api.DatastoresAPI(self)