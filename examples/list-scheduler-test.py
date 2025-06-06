import sage_data_client
import json

# lists all possible metrics associated with node W069 within the past hour
df = sage_data_client.query(
    start="2025-03-06T07:00:00.000Z",
    end="2025-03-07T07:00:00.000Z", 
    filter={
        "vsn": "W069",
        "name": "sys.scheduler.status.plugin.running",
    }
)

def extract(json_str, name):
    try:
        data = json.loads(json_str)
        return data.get(name, None)
    except (json.JSONDecodeError, TypeError):
        return None

def extract_plugin_image(json_str):
    return extract(json_str, 'plugin_image')

def extract_plugin_task(json_str):
    return "-".join(extract(json_str, 'plugin_task').split("-")[:-1])

print(df.iloc[2]["value"])
df['plugin_image'] = df['value'].apply(extract_plugin_image)
df['plugin_task'] = df['value'].apply(extract_plugin_task)

print(df["plugin_image"].unique())
print(df["plugin_task"].unique())

one_task = df["plugin_task"].unique()[0]
one_plugin = df["plugin_image"].unique()[0]

df = sage_data_client.query(
    start="2025-03-06T07:00:00.000Z",
    end="2025-03-07T07:00:00.000Z", 
    filter={
        "vsn": "W069",
        "task": one_task
    }
)

print(df)

df = sage_data_client.query(
    start="2025-03-06T07:00:00.000Z",
    end="2025-03-07T07:00:00.000Z", 
    filter={
        "vsn": "W069",
        "plugin": one_plugin
    }
)

print(df)