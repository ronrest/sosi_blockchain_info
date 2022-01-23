"""
Blockchain.info API
    https://www.blockchain.com/api/blockchain_apis

Base URL:
    https://blockchain.info

RATE LIMITS
-------
    - What are the API rate limits?

NOTES:
------
    Currently this only works for bitcoin information.
"""
from sosi_api import BaseClient
from sosi_api.utils import dt as dtutils
# import decouple
# import datetime

# Get environment variables
# env = decouple.AutoConfig(search_path="./.env")
# from urllib.parse import urlencode

class BlockchainInfoClient(BaseClient):
    def __init__(self, key=None):
        super().__init__(
            base_url="https://blockchain.info",
            headers=None,
            max_requests_per_min=5*60,
            response_kind="json",
        )
        # TODO: Allow the use of an api key
        # self.api_key = key if key is not None else env('BLOCKCHAIN_INFO_API_KEY', cast=str)

    def transaction(self, hash):
        """Get information for a transaction given its transaction hash id"""
        endpoint = f"/rawtx/{hash}"
        url = self.base_url + endpoint
        params = dict()
        response = self.request(url=url, params=params, kind="get")
        return response

    def transactions(self, address):
        """Get transactions for a given address.

        Notes: 
            This API endpoint returns a maximum of 50 records only.
            Need to implement pagination to get more.
        """
        endpoint = f"/rawaddr/{address}"
        url = self.base_url + endpoint
        limit = 50
        # TODO: implement pagination
        params = dict(
            limit=limit,
            offset=0,
        )
        response = self.request(url=url, params=params, kind="get")
        return response
