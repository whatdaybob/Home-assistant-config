# Automations
## [battery_charging.yaml](config/integrations/automations/battery_charging.yaml)

I have a battery charger plugged into a [Smartthings Smart Plug](https://amzn.to/3dWoZPe) and am monitoring its power usage. Occasionally I have forgotten to turn this on or swap the batteries over to ones that need charging so I set this automation up.

In short the charger idles at 5W and below, I have an automation that detects it is above 10W (charging) for 3 minutes and it notifies me. On the opposite if it drops back below 10W for 3 minutes it has completed charging and notifies me. 

Both automations have a condition not to fire if Home Assistants uptime is less than 5 minutes as I had issues getting notified after a server restart.