# xmc_api

##### Example:
```python
import xmc_api


exos_conn = xmc_api.Connection(
    'xmc_server',                   # XMC Server Address
    'exos_user'                     # Username
)

switch_list = exos_conn.switch_list_create('PNW')
```

##### Outputs
Will generate a list of dictionaries

```python
switch_list = [
    {
        'hostname': 'test-202-x590-r2',
        'host': '10.10.10.5',
        'groups': ['EXAMPLE_PCS_BUSINESS', 'PNW'],
        'neighbor': [],
        'data': {
            'location': 'EXAMPLE_DEPARTMENT',
            'role': 'EXAMPLE_CSW_DSW_ASW',
            'device_type': ''
        }
    },
    {
        'hostname': 'test-318-x450-s1',
        'host': '10.10.10.6',
        'groups': ['EXAMPLE_PCS_BUSINESS', 'PNW'],
        'neighbor': [],
        'data': {
            'location': 'EXAMPLE_DEPARTMENT',
            'role': 'EXAMPLE_CSW_DSW_ASW',
            'device_type': ''
        }
    }
]
```