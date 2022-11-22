from .base import BaseAPI

class DatastoresAPI(BaseAPI):
    def get_datastore(self, datastore_id: str) -> dict:
        r = self.ic.session.get(
            self.ic.base_url + "/data/data-store/" + datastore_id
        )

        r.raise_for_status()

        return r.json()['data']

    def get_all_datastores(self) -> dict:
        r = self.ic.session.get(
            self.ic.base_url + "/data/data-store"
        )

        r.raise_for_status()

        return r.json()['data']

    def add_row(self, datastore_id: str, data: dict) -> dict:
        r = self.ic.session.post(
            self.ic.base_url + "/data/data-store-collection",
            json={
                "data_store_id": datastore_id,
                "data": [
                    {
                        "_id": "",
                        "_uuid": "",
                        "_timestamp": "",
                        **data
                    }
                ]
            }
        )

        r.raise_for_status()

        return r.json()['data']

    def get_row(self, datastore_id: str, row_id: str) -> dict:
        return self.search_rows(
            datastore_id,
            filters=[{
                "fieldName": "_id",
                "fieldTypeName": "text",
                "operatorName": "=",
                "value": row_id
            }]
        )[0]

    def get_all_rows(self, datastore_id: str) -> dict:
        r = self.ic.session.post(
            self.ic.base_url + "/data/getdatastorecollection",
            json={
                "per_page": 10000,
                "data_store_id": datastore_id,
                "where": {
                    "maxDepth": 0,
                    "connectionType": "and",
                    "children": []
                },
                "row_limit": "no-limit"
            }
        )

        r.raise_for_status()

        return r.json()['ws_response_data']
    
    def search_rows(self, datastore_id: str, filters: list) -> dict:
        r = self.ic.session.post(
            self.ic.base_url + "/data/getdatastorecollection",
            json={
                "per_page": 10000,
                "data_store_id": datastore_id,
                "where": {
                    "maxDepth": 0,
                    "connectionType": "and",
                    "children": filters
                },
                "row_limit": "no-limit"
            }
        )

        r.raise_for_status()

        return r.json()['ws_response_data']

    def update_row(self, datastore_id: str, data_id: str, data: dict) -> None:
        r = self.ic.session.post(
            self.ic.base_url + "/data/bulk-update-documents",
            json={
                "data_store_id": datastore_id,
                "data": [
                    {
                        "_id": data_id,
                        "_uuid": "",
                        "_timestamp": 1234,
                        **data
                    }
                ]
            }
        )

        r.raise_for_status()

        return
