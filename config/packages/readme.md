# Packages
## [withings.yaml](./withings.yaml)
### details

The `withings` sensor platform consumes data from various health products produced by Withings. Currently I only own the [Withings Body Cardio](https://amzn.to/2Xa0FCw) scale but have been happy with it overall.

This is exposed as its own package as the integration has a template sensor to work with the data and I plan on expanding it more in future as I get more devices.

### defined entities 

* **sensor.withings_bone_mass_kg** - Bone mass from the scales
* **sensor.withings_fat_free_mass_kg**
* **sensor.withings_fat_mass_kg**
* **sensor.withings_fat_ratio_pct**
* **sensor.withings_heart_pulse_bpm**
* **sensor.withings_height_m**
* **sensor.withings_hydration**
* **sensor.withings_muscle_mass_kg**
* **sensor.withings_weight_kg** - The default weight measurement
* **sensor.withings_weight_stlb** - The default weight measurement converted to Stones and Pounds

<details><summary>Unused Sensors</summary>
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