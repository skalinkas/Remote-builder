from homeassistant.core import HomeAssistant
from .views import ESP32ViewCreatorRemotesView, ESP32AddRemoteView

DOMAIN = "esp32_view_creator"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the ESP32 View Creator component."""
    hass.data[DOMAIN] = {"remotes": []}

    # Register API views
    hass.http.register_view(ESP32ViewCreatorRemotesView(hass))
    hass.http.register_view(ESP32AddRemoteView(hass))

    # Register the custom panel
    hass.components.frontend.async_register_built_in_panel(
        component_name="esp32_view_creator",
        sidebar_title="ESP32 View Creator",
        sidebar_icon="mdi:remote",
        js_url="/custom_components/esp32_view_creator/static/esp32_view_creator.js",
    )

    return True
