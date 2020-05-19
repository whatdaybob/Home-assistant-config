# Packages
## [logger_set_levels.yaml](./logger_set_levels.yaml)

A package to allow me to change the logging level of HA and its components all via the UI.

<details><summary>Defined entities</summary>

* **input_select.log_integration:** - select this before changing the log level to only affect this integration.
* **input_select.log_level** - sets the log level of HA or the selected integration.

</details>
<details><summary>Automations</summary>

* **automation.logger_setdefaultlevel** - changes the log level to the one set in the input_select.
* **automation.logger_setdefault_component** - changes the log level to the one set in the input_select when an integration is selected.

</details>


## [media_server.yaml](./media_server.yaml)

Sets up all media related sensors. Nothing to fancy going on in here.

<details><summary>Defined entities</summary>

* **sensor.trakt_upcoming_calendar** - allows me to track my upcoming shows.
* **sensor.nzbget_[MULTI]** - all nzbget metrics and statistics.
* **sensor.sonarr_upcoming_media** - all episode sonarr is tracking.
* **sensor.plex_recently_added_movies** - new movies on the plex server.
* **sensor.plex_recently_added_movies** - new shows on the plex server.
* **sensor.youtube_[MULTI]** - sensor to show the latest videos from youtube channels.

</details>


## [mqtt_fix_retained_flag.yaml](./mqtt_fix_retained_flag.yaml)

Using all these MQTT devices is great but on the odd occasion (especially device name changes) you can end up with an issue caused by retained flags. This gives you the option to add a UI to fix this issue.

<details><summary>Defined entities</summary>

* **input_text.clear_mqtt_topic** - Type the topic to clear in this text box.

</details>

<details><summary>Automations</summary>

* **automation.clear_mqtt_topic** - checks as you type for a matching sensor, once found it sends a retained flag removal to that topic.

</details>


## [mqtt_iotlink_device.yaml]()

This is a package to manage Windows computers over MQTT. It uses the [IOT Link](https://iotlink.gitlab.io/) software on these devices to send and receive the messages.

<details><summary>Defined entities</summary>

* **binary_sensor.surface_book_connected** - uses LWT to see if device is connected to MQTT.
* **binary_sensor.surface_book_charging** - is it plugged in and charging
* **binary_sensor.surface_book_battery_status** - is it using battery atm?
* **camera.surface_book_screen_0** - a screen grab of current screen
* **camera.surface_book_screen_1** - if device has a second screen it will show a screen grab.
* **script.surface_book_displays_[on/off]** - scripts to toggle the screens.
* **script.surface_book_[MULTI]** - all the power control options.
* **script.surface_book_notify** - sends windows 10 ui notifications.
* **script.surface_book_vol_[max/mute]** - sets volume.
* **sensor.surface_book_boot_time** - system boot timestamp.
* **sensor.surface_book_cpu_usage** - percentage of CPU.
* **sensor.surface_book_current_user** - current logged in user name.
* **sensor.surface_book_hdd_[MULTI]** - all the HDD sensors you would need.
* **sensor.surface_book_idle_time** - how long the system has been idle
* **sensor.surface_book_ram_[MULTI]** - all the Ram sensors you would need.
* **sensor.surface_book_remaining_[battery/battery_time]** - battery sensors
* **sensor.surface_book_uptime** - uptime in human readable terms
* **switch.surface_book** - switch the computer on (WOL) and off (MQTT)

</details>

<details><summary>Automations</summary>

* **automation.iotlink_startup__device_** - refreshes the sensors on HA start via MQTT message.

</details>



## [mqtt_iotlink_officepc.yaml](./mqtt_iotlink_officepc.yaml)

See [mqtt_iotlink_device.yaml](#mqtt_iotlink_deviceyaml).

## [mqtt_iotlink_surfacebook.yaml](./mqtt_iotlink_surfacebook)

See [mqtt_iotlink_device.yaml](#mqtt_iotlink_deviceyaml).

## [mqtt_zigbee2mqtt.yaml](./mqtt_zigbee2mqtt.yaml)

This is a package that gives total control of [Zigbee2mqtt](https://www.zigbee2mqtt.io/).

<details><summary>Defined entities</summary>

* **switch.zigbee2mqtt_main_join** - starts a timer and permits joining the network.
* **sensor.zigbee2mqtt_github_version** - Zigbee2mqtt github version check.
* **sensor.zigbee2mqtt_networkmap** - populates the Zigbee2mqtt [zigbee2mqtt-networkmap](https://github.com/azuwis/zigbee2mqtt-networkmap).
* **sensor.zigbee2mqtt_bridge_state** - Zigbee2mqtt bridge status.
* **input_text.zigbee2mqtt_remove** - used with corresponding script to remove device from network.
* **input_text.zigbee2mqtt_[old/new]_name** - used with corresponding script to rename devices on the network.
* **input_select.zigbee2mqtt_log_level** - used with corresponding automation to set the log level.

</details>

<details><summary>Automations</summary>

* **automation.zigbee2mqtt_log_level** - sets the log level for debugging purposes.
* **automation.zigbee_join_enabled** - starts the timer to allow me to add to the network.
* **automation.zigbee_join_disabled** - stops the timer and resets the join switch.
* **automation.zigbee_successfull_interview** - notification on successful device joining.
* **automation.check_zigbee2mqtt_version** - updates the version sensor.

</details>


## [presence.yaml](./presence.yaml)

This one is a complex package as it uses a lot of moving parts.

<details><summary>Defined entities</summary>

* **device_tracker.phone__person_** - a device tracker using the icloud3 integration.
* **device_tracker._person__tado**  - a device tracker using the tado° integration.
* **input_select._person__tado** - for use in node red automations inspired by [philhawthorne](https://philhawthorne.com/making-home-assistants-presence-detection-not-so-binary/)
* **sensor.presence__person__last_changed** - using the person component to give a friendlier last changed status.

</details>
<details><summary>Automations</summary>

* **automation._person__away_homeassistant_start** - sets the input selects on start of HA to ensure they stay in sync.
* **automation._person__zone_entered** - sends a timestamp of when I enter a defined zone, used to see when I last visited a work client.

</details>

<details><summary>NodeRED</summary>
    
* Credit to [philhawthorne](https://philhawthorne.com/making-home-assistants-presence-detection-not-so-binary/) for the linking of device trackers to input selects.
    
    <details><summary>Presence Script</summary>

    ``` json
    [{"id":"9effc1aa.a34cd","type":"api-current-state","z":"87edcc21.c1486","name":"Status?","server":"b83e4413.7dc8c8","version":"1","outputs":1,"halt_if":"","halt_if_type":"str","halt_if_compare":"is","override_topic":false,"entity_id":"","state_type":"str","state_location":"payload","override_payload":"msg","entity_location":"data","override_data":"msg","blockInputOverrides":false,"x":555,"y":90,"wires":[["177a10ba.9ce64f","ca763488.1ccc68"]]},{"id":"177a10ba.9ce64f","type":"switch","z":"87edcc21.c1486","name":"Just Left?","property":"payload","propertyType":"msg","rules":[{"t":"neq","v":"Just Left","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":705,"y":75,"wires":[["c4b62bd1.420158"],["b7aba515.447dd8"]]},{"id":"ca763488.1ccc68","type":"change","z":"87edcc21.c1486","name":"RESET","rules":[{"t":"set","p":"reset","pt":"msg","to":"true","tot":"bool"}],"action":"","property":"","from":"","to":"","reg":false,"x":695,"y":130,"wires":[["6489f44e.bcfb4c","33a7b18c.83001e"]]},{"id":"c4b62bd1.420158","type":"api-call-service","z":"87edcc21.c1486","name":"Just Arrived","server":"b83e4413.7dc8c8","version":1,"debugenabled":false,"service_domain":"input_select","service":"select_option","entityId":"input_select.{{topic}}","data":"{\"option\":\"Just Arrived\"}","dataType":"json","mergecontext":"","output_location":"payload","output_location_type":"msg","mustacheAltTags":false,"x":850,"y":45,"wires":[["e721eb3.aa6fb18"]]},{"id":"d16c7a0b.6ad838","type":"api-call-service","z":"87edcc21.c1486","name":"Away","server":"b83e4413.7dc8c8","version":"1","debugenabled":false,"service_domain":"input_select","service":"select_option","entityId":"input_select.{{topic}}","data":"{\"option\":\"Away\"}","dataType":"json","mergecontext":"","output_location":"payload","output_location_type":"msg","mustacheAltTags":false,"x":845,"y":165,"wires":[["33a7b18c.83001e"]]},{"id":"92f56d0e.cb76a","type":"api-call-service","z":"87edcc21.c1486","name":"Extended Away","server":"b83e4413.7dc8c8","version":"1","debugenabled":false,"service_domain":"input_select","service":"select_option","entityId":"input_select.{{topic}}","data":"{\"option\":\"Extended Away\"}","dataType":"json","mergecontext":"","output_location":"payload","output_location_type":"msg","mustacheAltTags":false,"x":1145,"y":150,"wires":[[]]},{"id":"6489f44e.bcfb4c","type":"trigger","z":"87edcc21.c1486","op1":"","op2":"{\"payload\":{\"data\":{\"option\":\"\"}}}","op1type":"nul","op2type":"json","duration":"10","extend":false,"units":"min","reset":"","bytopic":"topic","name":"10 Min","x":695,"y":170,"wires":[["d16c7a0b.6ad838"]]},{"id":"33a7b18c.83001e","type":"trigger","z":"87edcc21.c1486","op1":"","op2":"{\"payload\":{\"data\":{\"option\":\"\"}}}","op1type":"nul","op2type":"json","duration":"24","extend":false,"units":"hr","reset":"","bytopic":"topic","name":"24 Hrs","x":995,"y":130,"wires":[["92f56d0e.cb76a"]]},{"id":"e721eb3.aa6fb18","type":"trigger","z":"87edcc21.c1486","op1":"","op2":"{\"payload\":{\"data\":{\"option\":\"\"}}}","op1type":"nul","op2type":"json","duration":"10","extend":false,"units":"min","reset":"","bytopic":"topic","name":"10 Min","x":995,"y":70,"wires":[["b7aba515.447dd8"]]},{"id":"b7aba515.447dd8","type":"api-call-service","z":"87edcc21.c1486","name":"Home","server":"b83e4413.7dc8c8","version":"1","debugenabled":false,"service_domain":"input_select","service":"select_option","entityId":"input_select.{{topic}}","data":"{\"option\":\"Home\"}","dataType":"json","mergecontext":"","output_location":"payload","output_location_type":"msg","mustacheAltTags":false,"x":1115,"y":90,"wires":[[]]},{"id":"d55fc4d5.75b8f8","type":"template","z":"87edcc21.c1486","name":"","field":"payload.entity_id","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"input_select.{{topic}}","output":"str","x":420,"y":90,"wires":[["9effc1aa.a34cd"]]},{"id":"104419cd.760ee6","type":"api-call-service","z":"87edcc21.c1486","name":"Just Left","server":"b83e4413.7dc8c8","version":1,"debugenabled":false,"service_domain":"input_select","service":"select_option","entityId":"input_select.{{topic}}","data":"{\"option\":\"Just Left\"}","dataType":"json","mergecontext":"","output_location":"payload","output_location_type":"msg","mustacheAltTags":false,"x":425,"y":190,"wires":[["6489f44e.bcfb4c","3c717fc3.bdf91"]]},{"id":"9e8106e8.fe5588","type":"switch","z":"87edcc21.c1486","name":"Home?","property":"status","propertyType":"msg","rules":[{"t":"eq","v":"home","vt":"str"},{"t":"eq","v":"not_home","vt":"str"}],"checkall":"false","repair":false,"outputs":2,"x":285,"y":150,"wires":[["d55fc4d5.75b8f8"],["104419cd.760ee6"]]},{"id":"a4a92e3b.3ce98","type":"change","z":"87edcc21.c1486","name":"Change","rules":[{"t":"move","p":"payload","pt":"msg","to":"status","tot":"msg"},{"t":"change","p":"topic","pt":"msg","from":"device_tracker.","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":145,"y":150,"wires":[["9e8106e8.fe5588"]]},{"id":"b1c49b45.da6ee8","type":"server-state-changed","z":"87edcc21.c1486","name":"Bob","server":"b83e4413.7dc8c8","version":"1","exposeToHomeAssistant":false,"haConfig":[{"property":"name","value":""},{"property":"icon","value":""}],"entityidfilter":"device_tracker.bob_tado","entityidfiltertype":"exact","outputinitially":false,"state_type":"str","haltifstate":"","halt_if_type":"str","halt_if_compare":"is","outputs":1,"output_only_on_state_change":false,"x":65,"y":75,"wires":[["a4a92e3b.3ce98"]]},{"id":"92eae36b.75797","type":"server-state-changed","z":"87edcc21.c1486","name":"Kay","server":"b83e4413.7dc8c8","version":1,"exposeToHomeAssistant":false,"haConfig":[{"property":"name","value":""},{"property":"icon","value":""}],"entityidfilter":"device_tracker.kay_tado","entityidfiltertype":"exact","outputinitially":false,"state_type":"str","haltifstate":"","halt_if_type":"str","halt_if_compare":"is","outputs":1,"output_only_on_state_change":false,"x":65,"y":30,"wires":[["a4a92e3b.3ce98"]]},{"id":"b83e4413.7dc8c8","type":"server","z":"","name":"Home Assistant","legacy":false,"rejectUnauthorizedCerts":false,"ha_boolean":"y|yes|true|on|home|open","connectionDelay":true,"cacheJson":true}]
    ```

    </details>

</details>

## [tado.yaml](./tado.yaml)

My favorite purchase so far is tado° as it offers so much! I use this for heating, presence detection, boiler usage and stats, open window monitoring and mold indicators.

<details><summary>Defined entities</summary>

* **climate._room_** - a climate device for every room of the house

    <details><summary>Templates using this sensor</summary>
    
    * **binary_sensor.landing_boiler** - is the boiler active
        
        <details><summary>Templates using this sensor</summary>
    
        * **sensor.cooling_hours_today** - history stats
        * **sensor.cooling_hours_two_days_ago** - history stats
        * **sensor.cooling_hours_yesterday** - history stats
        * **sensor.heating_hours_today** - history stats
        * **sensor.heating_hours_two_days_ago** - history stats
        * **sensor.heating_hours_yesterday** - history stats
        </details>

    </details>

* **sensor._room__early_start** - is early start heating enabled on this device
* **sensor._room__heating** - what percentage of heating is called for

    <details><summary>Templates using this sensor</summary>

    * **sensor.landing_boiler_heat_call** - how much heat is being called for from the boiler.
    </details>

* **sensor._room__humidity** - room humidity 

    <details><summary>Templates using this sensor</summary>

    * **sensor._room__mold** - indication for possible mold growth.
    </details>

* **sensor._room__link** - is the device connected
* **sensor._room__open_window** - is a window detected as open 

    <details><summary>Templates using this sensor</summary>

    * **binary_sensor._room__open_window** - used to pass data to homekit.
    </details>

* **sensor._room__overlay** - is this climate zone being manually set
* **sensor._room__power** - is the device powered
* **sensor._room__tado_mode** - climate mode
* **sensor._room__temperature** - room temperature

</details>

## [telegram_bot.yaml](./telegram_bot.yaml)

The `telegram` platform uses [Telegram](https://web.telegram.org/) to deliver notifications from Home Assistant to your supported devices. My implementation is just to get the basics up and running for now.

## [unifi_gateway_sensors.yaml](./unifi_gateway_sensors.yaml)

An all in one package for the [Unifi Gateway Custom Integration](https://github.com/custom-components/sensor.unifigateway/).
The Unifi Gateway Custom Integration connects to a Ubiquiti Controller instance to monitor high level health information on the setup including alerts and firmware updates.

<details><summary>Defined entities</summary>
<p>

* **sensor.unifi_gateway_wan** - Default WAN/USG sensor exposing multiple details
    <details><summary>Templates using this sensor</summary><p>

    * **sensor.unifi_gateway_uptime** - gets uptime in friendly terms
    * **sensor.unifi_gateway_cpu** - gets CPU usage percent
    * **sensor.unifi_gateway_memory** - gets memory usage percent
    * **sensor.unifi_gateway_wan_ip** - gets external IP address
    * **sensor.unifi_gateway_wan_download** - gets download amount in Kbps
    * **sensor.unifi_gateway_wan_upload** - gets upload amount in Kbps
    </p></details>
* **sensor.unifi_gateway_lan** - Default LAN sensor exposing multiple details
    <details><summary>Templates using this sensor</summary><p>
    
    * **sensor.unifi_lan_clients** - gets count of clients connected to the LAN
    </p></details>
* **sensor.unifi_gateway_wlan** - Default Wlan sensor exposing multiple details
    <details><summary>Templates using this sensor</summary><p>
    
    * **sensor.unifi_wlan_clients** - gets count of clients connected to the Wlan
    </p></details>
* **sensor.unifi_gateway_www** - Default WWW sensor exposing multiple details
    <details><summary>Templates using this sensor</summary><p>
    
    * **unifi_gateway_speedtest_ping** - gets speedtest ping results from the USG
    * **unifi_gateway_speedtest_upload** - gets speedtest upload results from the USG
    * **unifi_gateway_speedtest_download** - gets speedtest download results from the USG
    </p></details>
</p>
</details>



## [withings.yaml](./withings.yaml)

The `withings` sensor platform consumes data from various health products produced by Withings. Currently I only own the [Withings Body Cardio](https://amzn.to/2Xa0FCw) scale but have been happy with it overall.

This is exposed as its own package as the integration has a template sensor to work with the data and I plan on expanding it more in future as I get more devices.

<details><summary>Defined entities</summary>
<p>

* **sensor.withings_bone_mass_kg** - Bone mass from the scales
* **sensor.withings_fat_free_mass_kg**
* **sensor.withings_fat_mass_kg**
* **sensor.withings_fat_ratio_pct**
* **sensor.withings_heart_pulse_bpm**
* **sensor.withings_height_m**
* **sensor.withings_hydration**
* **sensor.withings_muscle_mass_kg**
* **sensor.withings_weight_kg** - The default weight measurement
    <details><summary>Templates using this sensor</summary><p>

    * **sensor.withings_weight_stlb** - The default weight measurement converted to Stones and Pounds
    </p></details>
</p>
</details>

<details><summary>Unused entities</summary>
<p>

#### Unpopulated due to not having a device to record measurements

* ~~**sensor.withings_body_temperature_c**~~
* ~~**sensor.withings_diastolic_blood_pressure_mmhg**~~
* ~~**sensor.withings_pulse_wave_velocity**~~
* ~~**sensor.withings_skin_temperature_c**~~
* ~~**sensor.withings_sleep_deep_duration_seconds**~~
* ~~**sensor.withings_sleep_heart_rate_average_bpm**~~
* ~~**sensor.withings_sleep_heart_rate_max_bpm**~~
* ~~**sensor.withings_sleep_heart_rate_min_bpm**~~
* ~~**sensor.withings_sleep_light_duration_seconds**~~
* ~~**sensor.withings_sleep_rem_duration_seconds**~~
* ~~**sensor.withings_sleep_respiratory_average_bpm**~~
* ~~**sensor.withings_sleep_respiratory_max_bpm**~~
* ~~**sensor.withings_sleep_respiratory_min_bpm**~~
* ~~**sensor.withings_sleep_tosleep_duration_seconds**~~
* ~~**sensor.withings_sleep_towakeup_duration_seconds**~~
* ~~**sensor.withings_sleep_wakeup_count**~~
* ~~**sensor.withings_sleep_wakeup_duration_seconds**~~
* ~~**sensor.withings_spo2_pct**~~
* ~~**sensor.withings_systolic_blood_pressure_mmhg**~~
* ~~**sensor.withings_temperature_c**~~

</p>
</details>