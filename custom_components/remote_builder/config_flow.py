from homeassistant import config_entries
from .const import DOMAIN

class RemoteBuilderConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Remote Builder."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Remote Builder", data={})
        return self.async_show_form(step_id="user")
