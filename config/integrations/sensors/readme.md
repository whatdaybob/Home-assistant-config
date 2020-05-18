# sensors
## [rest_intelnucmonitor.yaml](./rest_intelnucmonitor.yaml)
### details

This [Rest](https://www.home-assistant.io/integrations/rest/) sensor uses the [Home Assistant - Monitoring API](https://github.com/ned-kelly/ha-monitor-api/) for exposing the system's current metrics as my system is docker based and it doesn't have direct access to the host system. 

### defined entities

* **system cputemp** - Docker host system CPU temperature.
* **system cpuused** - Docker host system CPU usage.
* **system freegb** - Docker host system free drive space.
* **system driveused** - Docker host system used drive space.
* **system freemem** - Docker host system memory usage.
* **system networkin** - Docker host system download in GB.
* **system networkout** - Docker host system upload in GB.

## [steam_online.yaml](./steam_online.yaml)
### details

The `steam` sensor platform allow me to track the online status of public Steam accounts. I have added people I generally play with on steam or other platforms.

### defined entities
* **sensor.steam_UUID** - provides a steam users presence, last seen, user level and picture.

## [template_bins.yaml](./template_bins.yaml)
### details

I use [Node-RED](https://nodered.org/) to scrape the local councils bin schedule and provide Home Assistant with 3 sensor containing the next 3 collection dates of the general waste, recycling and garden waste. These are just timestamps so are not very friendly. 

![nodered bin sensor](/media/sensors_bins_screenshot.png)

Using templates I create better sensors with countdowns to collection and a bin week sensor with icon to match what week it is.

### defined entities
* **sensor.blue_bin** - countdown of days until general waste is collected.
* **sensor.brown_bin** - countdown of days until garden waste is collected.
* **sensor.grey_bin** - countdown of days until recycling is collected.
* **sensor.bin_week** - which bins are to be collected this week.

