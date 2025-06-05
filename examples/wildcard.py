import sage_data_client

# lists all possible metrics starting with sys.gps. associated with node W069 within the past hour
df = sage_data_client.query(
    start="-1h",
    filter={
        "name": "sys.gps.*",
        "vsn": "W069",
    }
)

# print(df)
print(df["name"].unique())
