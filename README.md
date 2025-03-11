# Python Sage/Waggle API Quick Start with Examples

## Prerequisites

Install the python [package](https://pypi.org/project/sage-data-client/) to access Sage Data Portal

```python3
pip3 install sage_data_client
```

## Querying

The query function accepts the following arguments:

- `start` Absolute or relative start timestamp. (required)
- `end` Absolute or relative end timestamp.
- `head` Limit results to head earliest values per series. (Only one of head or tail can be provided.)
- `tail` Limit results to tail latest values per series. (Only one of head or tail can be provided.)
- `filter` Key-value patterns to filter data on.

The returned object is a pandas dataframe

### API Quick Example

```python3
df = sage_data_client.query(
    start="-1h",                    # last hour
    filter={
        "name": "env.temperature",  # filter by metric
        "vsn": "W069|W097",         # and filter by node W069 or W097
    }
)
```

## Examples

> [!NOTE]  
> Occasionally some sensors maybe offline due to unforseen circumstances and fail to update the api service. Therefore, some of the examples thatuse `start="-1h"` may not always work.

`list-metrics.py` lists all possible metrics associated with node W069 within the past hour

`query-temperature.py` gets the env.temperature metric for all nodes within the past hour and shows the aggregate temperature associated with each node

`query-pressure-nodes.py` get the pressure associated with W069 and W097 between 3/6/2025 7AM UTC+0 to 2/7/2025 7AM UTC+0

`query-meta.py` get the value associated with the host (compute module in node) with matching description and sensor name

## Additional Resources

[sage_data_client](https://pypi.org/project/sage-data-client/) python package

[Sage Portal](https://portal.sagecontinuum.org/query-browser?start=-1m&page=0) for easy python snippet generation
