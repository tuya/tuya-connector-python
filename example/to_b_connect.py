"""This module has components that are used for testing to B connect."""
import logging
from tuya_connector.tuya_enums import TuyaCloudPulsarTopic
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,
)

ACCESS_ID = "xxxxx"
ACCESS_KEY = "xxxxx"

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init openapi and connect
openapi = TuyaOpenAPI("https://openapi.tuyacn.com", ACCESS_ID, ACCESS_KEY)
openapi.connect()
response = openapi.get("/v1.0/statistics-datas-survey", dict())

# Init Message Queue
open_pulsar = TuyaOpenPulsar(
    ACCESS_ID, ACCESS_KEY, "wss://mqe.tuyacn.com:8285/", TuyaCloudPulsarTopic.TEST
)
# Add Message Queue listener
open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

# Start Message Queue
open_pulsar.start()

input()
# Stop Message Queue
open_pulsar.stop()
