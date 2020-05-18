# Home Assistant Configuration by [@whatdaybob](https://github.com/whatdaybob) 


[Home Assistant](https://home-assistant.io/) configuration files.

This is my personal Home Assistant Configuration. I tinker here and there and hopefully am doing it correctly!

I will try and write a description for each folder as I add to it!

I have Home Assistant running on an [Intel NUC DN2820FYKH (Similar Model as mine is discontinued)](https://amzn.to/3cJvEMg)

**Software used in conjuction with Home Assistant:**

* [Mosquitto MQTT](https://mosquitto.org/) for [MQTT](https://en.wikipedia.org/wiki/MQTT) communications.
* [Mariadb](https://mariadb.org/) for the main database.
* [Adminer](https://www.adminer.org/) to manage the database.
* [Node-RED](https://nodered.org/) for automations and other things like cutom sensors.
* [Xbox-Smartglass-Core](https://github.com/OpenXbox/xbox-smartglass-core-python) for controlling xboxes.
* [Home Assistant - Monitoring API](https://github.com/ned-kelly/ha-monitor-api/) for exposing the system's current metrics via rest.
* [Zigbee2mqtt](https://www.zigbee2mqtt.io/) for controlling some zigbee devices
* [ha_dockermon](https://github.com/philhawthorne/ha-dockermon) to control docker containers directly in HA.
* [ESPHome](https://esphome.io/) for a few custom built sensors.
* [Prometheus](https://prometheus.io/) for storing long term sensor data.
* [Grafana](https://grafana.com/) for viewing the long term sensor data in pretty graphs.
* [cAdvisor](https://github.com/google/cadvisor/blob/master/docs/storage/prometheus.md) for exposing my docker and hardware statistics for more graphs.
* [Node exporter](https://prometheus.io/docs/guides/node-exporter/) for monitoring linux host metrics in prometheus.
* [Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) for handling metrics alerts.
* [Dozzle](https://dozzle.dev/) for viewing log files for my docker containers in a browser.
* [unifi-poller](https://github.com/unifi-poller/unifi-poller) for sharing Unifi data with prometheus.
* [AdGuard Home]() for network DNS management.

*A lot of these just send data to prometheus but come back in via alermanager webhooks*

**Devices in Use:**

#### Alexa Echo Devices
* [Amazon Echo](https://amzn.to/3fSFcXv) in the hallway for general usage
* [Echo Dots](https://amzn.to/2TcQjR6) in majority of the other rooms

#### Remotes and Hubs
* [Logitech Harmony Elite](https://amzn.to/2WDaQ3C) for controlling living room media centre.
* [SmartThings Hub](https://amzn.to/3cIu5hH) is used for its Z-Wave and simple app.

## Lights
### Philips Hue
* [Hue Bridge](https://amzn.to/366TuPE) came with starter kit. WAF means I am keeping this for now.
* [Philips Hue Smart Wireless Dimmer Switch](https://amzn.to/2TeRKP8) for ease of use. WAF again.
* [Philips Hue White Ambiance Standard Bulbs](https://amzn.to/2WGGiht) but may upgrade to colour eventually.
* [Philips Hue White Ambiance GU10 Bulbs](https://amzn.to/3g8pqYG) for downlights.
### Other
* Lightpack2 for ambilight, unsure where to link but the [Philips Hue Play HDMI Sync Box](https://amzn.to/2X5HPMX) is similar.

### Media Players
* [SkyQ](https://www.sky.com/shop/tv/sky-q/) pretty much defacto in the UK.
* [Sonos One](https://amzn.to/3dSmI7B) for great sound and inbuilt Alexa/Google Assistant
* [Sonos Beam](https://amzn.to/2TeKKl8) for media centre with inbuilt Alexa/Google Assistant, night mode and speech enhancements.
* [Nvidia Shield](https://amzn.to/3dU9JlL) acts as the main media device and also is a great plex server.

### Climate
* [tado° Internet Bridge](https://amzn.to/2TfMcDW) links all devices, part of the starter kit.
* [tado° Thermostat](https://amzn.to/2ZeYuAy) is used in the larger rooms as you can link TRVs to it.
* [tado° TRVs](https://amzn.to/2TfXzMf) in every room that has a radiator.
* [tado° Extension Kit](https://amzn.to/3dVJKua) to allow my boiler to be controlled.

### Network
* [Ubiquiti Networks UBI-UAP-AC-PRO](https://amzn.to/3cIh9Z4) is the main access point in the house.
* [Ubiquiti Networks Unifi Security Gateway Router](https://amzn.to/2WD5WDD) is the dhcp server etc.
* [Ubiquiti USW-FLEX Switch](https://amzn.to/2zQzMLO) are located in my office and the media centre


### Sensors
* [Withings Body Cardio](https://amzn.to/2Xa0FCw) gets me generic health data.

* Apple/iOS Devices - [iPhone 11](https://amzn.to/2X5z59t), [iPhone 8](https://amzn.to/2TfaQou) & [iPads](https://amzn.to/2X0aXoQ)
* [Philips Hue Motion](https://amzn.to/2zLUpsG)
* [Smartthings Door Sensor](https://amzn.to/369TkqO)
* [Xbox One](https://amzn.to/3bIkxSB) for bedroom gaming.
* [Xbox One X](https://amzn.to/2LAxpzo) for living room gaming.
* [Aeon Labs Home Energy Meter](https://amzn.to/2z4BTf2)
* [Aqara Door Window Sensor](https://amzn.to/3bFSkMf)
* [Aqara Button](https://amzn.to/2LzhSQw)


If i helped in anyway and you would like to help me, consider donating a lovely beverage with the below.

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 20px !important;letter-spacing:-0.08px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Lato', sans-serif !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Lato&subset=latin,latin-ext" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/whatdaybob"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:19px !important;">Buy me a coffee</span></a>