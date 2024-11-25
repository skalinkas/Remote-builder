from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_HOST
import voluptuous as vol

DOMAIN = "esp32_view_creator"

class ESP32ViewCreatorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for ESP32 View Creator."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Create the config entry
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): str,
                    vol.Required(CONF_HOST): str,
                }
            ),
        )
