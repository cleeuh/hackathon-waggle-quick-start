import sage_data_client

# lists all possible metrics associated with node W069 within the past hour
df = sage_data_client.query(
    start="-1h",
    filter={
        "vsn": "W069",
    }
)

print(df)
print(df["name"].unique())
