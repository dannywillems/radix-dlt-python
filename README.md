# DO NOT USE - WIP

[![Build Status](https://travis-ci.org/dannywillems/radix-dlt-python.svg?branch=master)](https://travis-ci.org/dannywillems/radix-dlt-python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc14f0cc741e45f38d633e7d4e7fd12a)](https://www.codacy.com/manual/dannywillems/radix-dlt-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dannywillems/radix-dlt-python&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/dannywillems/radix-dlt-python/badge.svg)](https://coveralls.io/github/dannywillems/radix-dlt-python)

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.4](https://img.shields.io/badge/python-3.4-blue.svg)](https://www.python.org/downloads/release/python-340/)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

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
