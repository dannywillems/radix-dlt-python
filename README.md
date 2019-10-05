# DO NOT USE - WIP

## Setup environment

```shell
mkvirtualenv radixdlt-dev
workon radixdlt-dev
pip install -e .
```

## Connect to a client

### In a specific universe

```python
from radixdlt.universe.register import REGISTER

Sunstone = REGISTER.get("sunstone")
client = Sunstone.get_client_using_finder()
```

### Using the IP and the universe

```python
from radixdlt.network.client import SunstoneClient

client = SunstoneClient(client_ip="localhost")
```
