# Packages
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