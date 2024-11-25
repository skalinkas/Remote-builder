from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .views import ESP32ViewCreatorRemotesView

DOMAIN = "esp32_view_creator"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the ESP32 View Creator component."""
    hass.data[DOMAIN] = {"remotes": []}

    # Register the API view
    hass.http.register_view(ESP32ViewCreatorRemotesView(hass))

    # Register the custom panel
    hass.components.frontend.async_register_built_in_panel(
        component_name="esp32_view_creator",
        sidebar_title="ESP32 View Creator",
        sidebar_icon="mdi:remote",
        js_url="/custom_components/esp32_view_creator/static/esp32_view_creator.js",
    )

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up ESP32 View Creator from a config entry."""
    hass.data[DOMAIN]["remotes"].append(entry.data)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload an ESP32 View Creator config entry."""
    hass.data[DOMAIN]["remotes"].remove(entry.data)
    return True
