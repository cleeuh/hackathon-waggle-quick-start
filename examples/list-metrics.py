import sage_data_client

# lists all possible metrics associated with node W069 within the past hour
df = sage_data_client.query(
    start="-1h",
    filter={
        "vsn": "W069",
        # "name": "",
        # "task": "",
        # "plugin": "",
    }
)

print(df, "\n")
print(df["name"].unique(), "\n")
print(df["meta.task"].unique(), "\n")
print(df["meta.plugin"].unique(), "\n")
