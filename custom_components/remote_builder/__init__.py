from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Remote Builder integration from YAML."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Remote Builder from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Register the sidebar panel
    hass.http.register_static_path(
        "/remote-builder-panel",
        hass.config.path("custom_components/remote_builder/www"),
        cache_headers=False,
    )
    hass.components.frontend.async_register_built_in_panel(
        "iframe",
        DOMAIN,
        "mdi:remote",
        config={"url": "/remote-builder-panel/index.html"},
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    if DOMAIN in hass.data:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
