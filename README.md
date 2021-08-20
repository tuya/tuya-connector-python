# tuya-connector-python

The `tuya-connector-python` SDK is desinged to support open APIs and Pulsar Messages provided by Tuya. Before using, you can read more about Tuya cloud Development by accessing [official documentation](https://developer.tuya.com/en/docs/iot/quick-start1?id=K95ztz9u9t89n).

## Installation

  `pip3 install tuya-connector-python`

## Getting Started

1. [Sign up for tuya developer account](https://auth.tuya.com/register?from=https%3A%2F%2Fiot.tuya.com%2F).
2. [Create a cloud project](https://iot.tuya.com/cloud/), get the authorization key and other necessary parameters.
3. Quick Example:


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
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Call any API from Tuya
response = openapi.get("/v1.0/statistics-datas-survey", dict())

# Init Message Queue
open_pulsar = TuyaOpenPulsar(
    ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
)
# Add Message Queue listener
open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

# Start Message Queue
open_pulsar.start()

input()
# Stop Message Queue
open_pulsar.stop()

```

## Tuya Open API Reference

Tuya opens up a variety of APIs covering business scenarios such as device pairing, asset management, and device control. You can call APIs according to API integration documents to implement applications.

For more information, see the [documentation](https://developer.tuya.com/en/docs/cloud/?_source=github).
<!-- [Documentation > Cloud Development > API Reference](https://developer.tuya.com/docs/iot/open-api/api-reference/api-reference) -->


## Issue Feedback

You can provide feedback on your issue via **Github Issue** or [Technical Ticket](https://service.console.tuya.com/).

## License

tuya-iot-py-sdk is available under the MIT license. Please see the [LICENSE](./LICENSE) file for more information.
