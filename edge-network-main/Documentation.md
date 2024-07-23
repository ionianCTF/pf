# MQTT broker

Ο MQTT broker δέχεται requests στα εξής channels:
* devices/{sensor_id}/wifi
* devices/{sensor_id}/bluetooth/clasic
* devices/{sensor_id}/bluetooth/ble

όπου _sensor_id_ είναι το διακριτικό το sensor (raspberry) που στέλνει τα δεδομένα.

## WiFi json response

```
[
  [WiFi data],
  [WiFi data],
   ….
]
```

_WiFi data_ is defined as:
* MAC Address : encoded string using sha256
* Device Name : encoded string using sha256 
* Distance: number that represents the distance in meters from the raspberry.
* Capabilities: string describing the capabilities of the device 

Sample Output
```
[
  [
    "b4545a46c54654",
    "34535b4564c879d",
    1.25,
    “short-slot+ESS+privacy”
  ],
  [
    "c4678945d46c54654",
    "657a465b234c",
    0.45,
    “Probe Response (res8+short-slot+ESS+privacy)”
  ]
……
]
```

## Bluetooth json response
```
[
  [Bluetooth data],
  [Bluetooth data],
   ….
]
```
_Bluetooth data_ is defined as:
* MAC Address : encoded string using sha256
* Device Name : encoded string using sha256
* Signal strength : number
Zero (0) value indicates that the strength value is not available.

Sample Output

```
[
  [
    "b4545a46c54654",
    "34535b4564c879d",
    0
  ],
  [
    "c4678945d46c54654",
    "657a465b234c",
    0
  ]
……
]
```

