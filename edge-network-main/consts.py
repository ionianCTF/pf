# Sensor Related
sensor_id = "CMODLAB"

# MQTT related
#mqtt_broker_address = "mqtt-peopleflows.cmodlab-iu.edu.gr"
mqtt_broker_address = "mqtt.eclipseprojects.io"
wifi_topic = "devices/" + sensor_id + "/wifi"
clasic_bluetooth_topic = "devices/" + sensor_id + "/bluetooth/clasic"
ble_bluetooth_topic = "devices/" + sensor_id + "/bluetooth/ble"


# Other
wifi_interface = "mon1"
bluetooth_interface = "hci0"
scan_duration = 15
