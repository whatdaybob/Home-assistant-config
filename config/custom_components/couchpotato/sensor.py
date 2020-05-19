"""Platform for sensor integration."""
import logging
from datetime import datetime

import requests
import json
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.components.switch import PLATFORM_SCHEMA
from homeassistant.const import *

_LOGGER = logging.getLogger(__name__)
DEFAULT_LIMIT = 10
DEFAULT_STATE = "active"
DEFAULT_NAME = "CouchPotato"
DEFAULT_HOST = "localhost"
DEFAULT_PROTO = "http"
DEFAULT_PORT = "5050"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_TOKEN): cv.string,
    vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.string,
    vol.Optional(CONF_HOST, default=DEFAULT_HOST): cv.string,
    vol.Optional(CONF_PROTOCOL, default=DEFAULT_PROTO): cv.string,
    vol.Optional(CONF_MAXIMUM, default=DEFAULT_LIMIT): cv.string,
    vol.Optional(CONF_STATE, default=DEFAULT_STATE): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([CouchPotatoSensor(config)])


class CouchPotatoSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, config):
        self._state = None
        self._name = config.get(CONF_NAME)
        self.token = config.get(CONF_TOKEN)
        self.host = config.get(CONF_HOST)
        self.protocol = config.get(CONF_PROTOCOL)
        self.port = config.get(CONF_PORT)
        self.data = None
        self.state_movies = config.get(CONF_STATE)
        self.limit = config.get(CONF_MAXIMUM)

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.data

    def update(self):
        attributes = {}
        card_json = []

        init = {}
        """Initialized JSON Object"""
        init['title_default'] = '$title'
        init['line1_default'] = '$episode'
        init['line2_default'] = '$release'
        init['line3_default'] = '$number - $rating - $runtime'
        init['line4_default'] = '$genres'
        init['icon'] = 'mdi:eye-off'
        card_json.append(init)

        ifs_movies = self.get_infos(self.protocol, self.host, self.port, self.token)

        for movie in ifs_movies['movies']:
            card_items = {}
            if "released" in movie['info']:
                card_items['airdate'] = movie['info']['released']
            else:
                card_items['airdate'] = datetime.fromtimestamp(movie['info']['release_date']['expires']).strftime(
                    "%Y-%m-%d")
            card_items['episode'] = ""
            card_items['release'] = "$day, $date $time"
            if "original_title" in movie['info']:
                card_items["title"] = movie['info']['original_title']
            if "genres" in movie['info']:
                card_items["genres"] = ', '.join(map(str, movie['info']['genres']))
            if "rating" in movie['info']:
                card_items['rating'] = ('\N{BLACK STAR} ' + str(movie['info']['rating']['imdb'][0]))
            if "poster_original" in movie['info']['images'] and len(movie['info']['images']['poster_original']) != 0:
                card_items["poster"] = movie['info']['images']['poster_original'][0]
            elif "poster" in movie['info']['images'] and len(movie['info']['images']['poster']) != 0:
                card_items["poster"] = movie['info']['images']['poster'][0]
            else:
                card_items["poster"] = ""
            if "runtime" in movie['info']:
                card_items['runtime'] = movie['info']["runtime"]
            card_json.append(card_items)
        attributes['data'] = json.dumps(card_json)
        if ifs_movies["success"].__eq__("True"):
            self._state = "Success"
        else:
            self._state = "Failure"
        self.data = attributes

    def get_infos(self, proto, host, port, token):
        url = "{0}://{1}:{2}/api/{3}/media.list/?status={4}&type=movie&limit_offset={5}".format(
            proto,
            host, port, token, self.state_movies,
            self.limit)
        ifs_movies = requests.get(url).json()
        return ifs_movies
