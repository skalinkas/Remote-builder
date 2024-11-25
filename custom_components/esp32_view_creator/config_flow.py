from homeassistant import config_entries

class ESP32ViewCreatorConfigFlow(config_entries.ConfigFlow, domain="esp32_view_creator"):
    """ESP32 View Creator config flow."""
    async def async_step_user(self, user_input=None):
        """Handle user setup."""
        return self.async_create_entry(title="ESP32 View Creator", data={})
