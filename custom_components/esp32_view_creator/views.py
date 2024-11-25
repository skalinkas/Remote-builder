from homeassistant.components.http import HomeAssistantView

DOMAIN = "esp32_view_creator"

class ESP32ViewCreatorRemotesView(HomeAssistantView):
    """Handle requests for the list of remotes."""

    url = "/api/esp32_view_creator/remotes"
    name = "api:esp32_view_creator:remotes"

    def __init__(self, hass):
        """Initialize the view."""
        self.hass = hass

    async def get(self, request):
        """Handle GET requests."""
        remotes = self.hass.data[DOMAIN]["remotes"]
        return self.json(remotes)
