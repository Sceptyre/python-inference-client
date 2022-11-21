# Usage
### Connect
```py
from inferenceclient import InferenceClient
client = InferenceClient(
    username="username",
    secret="secret",
    apikey="apikey"
)
```

### Examples
#### Get Datastore
```py
client.datastores.get_datastore(
    datastore_id='123'
)
```
Response
```json
[
    {
        'id': '123',
        'name': 'DATASTORE_NAME',
        'configurable': 'yes'
    }
]
```
#### Get Datastore Row
```py
client.datastores.get_row(
    datastore_id='123',
    row_id='1'
)
```
Response
```json
[
    {
        'id': '1',
        'uuid': None,
        'instance_id': '0',
        'timestamp': '2022-11-21 00:00:00',
        'col_1': 'val_1',
        'col_2': 'val_2'
    }
]
```