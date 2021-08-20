# tuya-connector-python

The `tuya-connector-python` SDK is desinged to support open APIs and Pulsar Messages provided by Tuya. Before using, you can read more about cloud project configuration by accessing [official tutorial](https://developer.tuya.com/en/docs/iot/device-control-practice?id=Kat1jdeul4uf8).

Quick Example:

``` python
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
)

ACCESS_ID = "your-access-id"
ACCESS_KEY = "your-access-key"
API_ENDPOINT = "https://openapi.tuyacn.com"
MQ_ENDPOINT = "wss://mqe.tuyacn.com:8285/"

# Init openapi and connect
openapi = TuyaOpenAPI("API_ENDPOINT", ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call any API from Tuya
response = openapi.get("/v1.0/statistics-datas-survey", dict())

# Init Message Queue
open_pulsar = TuyaOpenPulsar(
    ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.TEST
)
# Add Message Queue listener
open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

# Start Message Queue
open_pulsar.start()

input()
# Stop Message Queue
open_pulsar.stop()

```
