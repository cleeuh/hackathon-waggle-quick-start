import sage_data_client

# get the value associated with the host (compute module in node) with matching description and sensor name
df = sage_data_client.query(
    start="-1h",
    filter={
        "host": "000048b02d3ae2db.ws-nxcore",       # filter by meta.host
        "description": "Ambient Relative Humidity", # and filter by meta.description
        "sensor": "vaisala-aqt530",                 # and filter by meta.sensor
    }
)

print(df)
print(df.value)
