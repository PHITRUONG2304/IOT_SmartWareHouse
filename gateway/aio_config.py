from Adafruit_IO import MQTTClient
AIO_USERNAME = "truongtruong230401"
AIO_KEY = "aio_pBjf329XkJ3rv5WymAN1NAWejkYQ"

FEED_TEMP = "smart-warehouse.bbc-temp"
FEED_HUMIDITY = "smart-warehouse.bbc-humi"
FEED_LIGHT = "smart-warehouse.bbc-light"
FEED_GAS = "smart-warehouse.bbc-gas"

client = MQTTClient(AIO_USERNAME, AIO_KEY)
