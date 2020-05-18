# customize
### Used to further edit entities

I have split all my customize files out by domain as I use a script in the `developer-tools` > `template` section in HA to create the files. 

Firstly you need to know what domains you have (you may know) as I had too many to remember on the fly. This script outputs all domains to a list, unfortunately I cant filter it as appending lists is not allowed.

``` jinja
{% for state in states %}
    {{-state.domain}}
{% endfor %}
```
Once you have your list replace `|||DOMAIN|||` in the below script and you will have a customize file almost created.

``` jinja
{% for state in states.|||DOMAIN||| %}
{% if loop.first %}
#############################################
# {{state.domain}}
#############################################

{% else %}
{% endif %}
{{- state.entity_id }}:
  {% if state.attributes.friendly_name is defined %}friendly_name: {{ state.attributes.friendly_name|replace("_"," ",)|title()}}{% else %}friendly_name: {{ state.name|replace("_"," ",)|title() }}{% endif -%}
  {% if state.attributes.hidden is defined %}\nhidden: {{ state.attributes.hidden }}{% endif -%}
  {% if state.domain != "media_player" %}{% if state.attributes.entity_picture is defined %}\nentity_picture: {{ state.attributes.entity_picture }}{% endif -%}{% endif -%}
  {% if state.domain != "media_player" %}{% if state.attributes.icon is defined %}\nicon: {{ state.attributes.icon }}{% endif -%}{% endif -%}
  {% if state.attributes.assumed_state is defined %}\nassumed_state: {{state.attributes.assumed_state}}{% endif -%}
  {% if state.attributes.initial_state is defined %}\ninitial_state: {{state.attributes.initial_state}}{% endif -%}
  {% if state.attributes.device_class is defined %}\ndevice_class: {{state.attributes.device_class}}{% endif -%}
  {% if state.attributes.unit_of_measurement is defined %}\nunit_of_measurement: {{state.attributes.unit_of_measurement}}{% endif -%}
{% endfor %}
```
In my example I have used counter. 
You will however notice that there is a `\n` where a new line is needed. 

![new line issue](/media/customize_screenshot_1.png)

In VSCode I can easily fix these with the multi cursor editing using `CTRL+F`, typing in `\n` then pressing `ALT+ENTER` to select them all then press `ENTER` which inserts a new line and auto tabs it.