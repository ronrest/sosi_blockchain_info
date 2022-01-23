# Usage


## Connect to Client

```python
from sosi_blockchain_info import BlockchainInfoClient
client = BlockchainInfoClient()
```

## Usage

```python
# GET INFORMATION FOR A SPECIFIC TRANSACTION
transaction_hash = "XXX"
client.transaction(transaction_hash)
```

[Example Transaction Response](responses/transaction.md)

```python
# GET TRANSACTIONS FOR A WALLET ADDRESS
wallet_address = "XXX"
client.transactions(wallet_address)
```

[Example Wallet Adddress Transactions Response](responses/address_transactions.md)
