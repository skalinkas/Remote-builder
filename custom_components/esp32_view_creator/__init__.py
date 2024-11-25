from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "esp32_view_creator"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the ESP32 View Creator component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up ESP32 View Creator from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload an ESP32 View Creator config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
