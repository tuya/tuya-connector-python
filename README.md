# tuya-connector-python

![PyPI](https://img.shields.io/pypi/v/tuya-connector-python)

![PyPI - Downloads](https://img.shields.io/pypi/dm/tuya-connector-python)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tuya-connector-python)

The `tuya-connector-python` SDK is designed to support openAPIs and Pulsar messages provided by Tuya. Before using this SDK, you can see [Quick Start](https://developer.tuya.com/en/docs/iot/quick-start1?id=K95ztz9u9t89n) on the Tuya Developer website to learn more about Cloud Development Platform.

## Install

`pip3 install tuya-connector-python`

## Get started

1. [Sign up](https://auth.tuya.com/register?from=https%3A%2F%2Fiot.tuya.com%2F) for Tuya developer account.

2. [Create a cloud project](https://iot.tuya.com/cloud/). See the [tutorial](https://developer.tuya.com/en/docs/iot/device-control-practice?id=Kat1jdeul4uf8) for how to get the authorization key and other necessary parameters.

3. A quick example is as follows:

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
   
   # Init OpenAPI and connect
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

## OpenAPI reference

Tuya opens up a variety of APIs covering scenarios such as device pairing, asset management, and device control. You can call APIs according to [API reference](https://developer.tuya.com/en/docs/cloud/?_source=github) to create IoT applications.

## Feedback

If you have any questions, please provide feedback via **Github Issue** or [Technical Ticket](https://service.console.tuya.com/).

## License

The `tuya-connector-python` SDK is available under the MIT license. For more information, see the [LICENSE](./LICENSE) file.
