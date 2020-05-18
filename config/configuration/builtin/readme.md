# Builtin Configuration
## frontend.yaml
#### [Link to details](https://www.home-assistant.io/integrations/frontend/)

All i have defined in the `frontend` is the themes location

## history.yaml
#### [Link to details](https://www.home-assistant.io/components/history/)

The `history` integration will track everything that is going on within Home Assistant and allows the user to browse through it.

I keep the history trimmed down as too much history slows down the frontend. By default I am tracking a few domains and exclude majority of sensors and track only the ones I find important.

## homeassistant.yaml
#### [Link to details](https://www.home-assistant.io/docs/configuration/basic/)

This file holds the main configuration variables for the system. In here I have defined the package and customize folders as well as auth settings.

## homekit.yaml
#### [Link to details](https://www.home-assistant.io/integrations/homekit/)

The `homekit` integration allows you to forward entities from Home Assistant to Apple HomeKit, so they can be controlled from Apple’s Home app and Siri.

I have only defined and customised sensors I feel I would need in the home app. One thing of note is that the media player I created in the [livingroom_mediacentre package](config/packages/livingroom_mediacentre.yaml) is customized to be exposed as a TV.

## http.yaml
#### [Link to details](https://www.home-assistant.io/integrations/http/)

The `http` integration serves all files and data required for the Home Assistant frontend. 

In here it is best to set a `base_url` and any proxy settings you need to expose your system to the outside world.

## logbook.yaml
#### [Link to details](https://www.home-assistant.io/integrations/logbook/)

The `logbook` integration provides a different perspective on the history of your house by showing all the changes that happened to your house in reverse chronological order.

As with history I have trimed this down as I dont want certain sensors filling this page up.

## logger.yaml
#### [Link to details](https://www.home-assistant.io/integrations/logger/)

The `logger` integration lets you define the level of logging activities in Home Assistant.

I have it default to warn but can set it via the front end using the [logger_set_levels](config/packages/logger_set_levels.yaml) package.

## prometheus.yaml
#### [Link to details](https://www.home-assistant.io/integrations/prometheus/)

The `prometheus` integration exposes metrics in a format which Prometheus can read.

As Prometheus cant accept all data this is trimmed to the essentials. I use `component_config_glob` to tell Prometheus what the data is.

## recorder.yaml
#### [Link to details](https://www.home-assistant.io/integrations/recorder/)

The `recorder` integration is responsible for storing details in a database, which then are handled by the history integration.

I have trimmed this down to help the database stay clean.

## system_log.yaml
#### [Link to details](https://www.home-assistant.io/integrations/system_log/)

The `system_log` integration stores information about all logged errors and warnings in Home Assistant. 

I have this setup with `fire_event: true` so I can count errors in the logs using counters and automations in the [hass_system](config/packages/hass_system.yaml) package.

## tts.yaml
#### [Link to details](https://www.home-assistant.io/integrations/tts)

Text-to-Speech (TTS) enables Home Assistant to speak to you. I have not used this yet but plan to.

## utility_meter.yaml
#### [Link to details](https://www.home-assistant.io/integrations/utility_meter/)

The `utility meter` integration provides functionality to track consumptions of various utilities (e.g., energy, gas, water, heating).

I am using an [Aeon Labs Home Energy Meter](https://amzn.to/2z4BTf2) paired to my [SmartThings Hub](https://amzn.to/3cIu5hH) via Z-Wave to collect energy data and use this to display it in a friendly way.

