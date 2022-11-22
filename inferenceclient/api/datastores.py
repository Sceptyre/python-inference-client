from .base import BaseAPI

class DatastoresAPI(BaseAPI):
    def get_datastore(self, datastore_id: str) -> dict:
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/list-one',
            params={
                'datastore_id': datastore_id
            }
        )

        return r

    def get_all_datastores(self) -> dict:
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/list-all'
        )

        return r

    def add_row(self, datastore_id: str, data: dict) -> None:
        self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/add-row',
            params={
                'datastore_id': datastore_id,
                'data': data
            }
        )

    def get_row(self, datastore_id: str, row_id: str) -> dict:
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/list-one-row',
            params={
                'datastore_id': datastore_id,
                'data_id': row_id
            }
        )

        return r

    def get_all_rows(self, datastore_id: str) -> dict:
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/list-all-rows',
            params={
                'datastore_id': datastore_id
            }
        )

        return r
    
    def search_rows(self, datastore_id: str, filters: list) -> dict:
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/search',
            params={
                'datastore_id': datastore_id,
                'filters': filters
            }
        )

        return r

    def update_row(self, datastore_id: str, data_id: str, data: dict):
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/update-row',
            params={
                'datastore_id': datastore_id,
                'data_id': data_id,
                'data': data
            }
        )

        return r

    def delete_row(self, datastore_id: str, data_id: str):
        r = self.ic._query(
            path='https://usstudio.inferencecommunications.com/studio_instance/studio-api/v1/datastore/delete-row',
            params={
                'datastore_id': datastore_id,
                'data_id': data_id
            }
        )

        return r
