from homeassistant.components.http import HomeAssistantView
import json

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


class ESP32AddRemoteView(HomeAssistantView):
    """Handle requests to add a new remote."""

    url = "/api/esp32_view_creator/add_remote"
    name = "api:esp32_view_creator:add_remote"

    def __init__(self, hass):
        """Initialize the view."""
        self.hass = hass

    async def post(self, request):
        """Handle POST requests."""
        body = await request.json()
        name = body.get("name")
        host = body.get("host")

        if not name or not host:
            return self.json_message("Invalid data", 400)

        # Add the remote to the list
        self.hass.data[DOMAIN]["remotes"].append({"name": name, "host": host})
        return self.json_message("Remote added", 201)
