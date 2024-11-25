from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
import voluptuous as vol

DOMAIN = "esp32_view_creator"

class ESP32ViewCreatorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """ESP32 View Creator config flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="ESP32 View Creator", data=user_input)

        # Show a form for entering the configuration
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Optional(CONF_PORT, default=80): int,
                }
            ),
        )
