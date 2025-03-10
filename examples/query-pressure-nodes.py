import sage_data_client

# get the pressure associated with W069 and W097 between 3/6/2025 7AM UTC+0 to 2/7/2025 7AM UTC+0
df = sage_data_client.query(
    start="2025-03-06T07:00:00.000Z",
    end="2025-03-07T07:00:00.000Z", 
    filter={
        "name": "env.pressure", # filter by env.pressure metric
        "vsn": "W069|W097",     # and filter by node W069 or W097
    }
)

print(df)
