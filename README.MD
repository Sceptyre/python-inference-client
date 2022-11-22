# Install
`pip install git+https://github.com/Sceptyre/python-inference-client.git@v0.0.1`

# Usage
### Connect
```py
from inferenceclient import InferenceClient
client = InferenceClient(
    apikey="apikey",
    account_id="1234"
)
```

### Examples
#### Get Datastore
```py
client.datastores.get_datastore(
    datastore_id='123'
)
```
#### Get Datastore Row
```py
client.datastores.get_row(
    datastore_id='123',
    row_id='a1b2c3'
)
```