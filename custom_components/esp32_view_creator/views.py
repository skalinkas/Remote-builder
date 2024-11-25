from homeassistant.helpers import config_validation as cv
from homeassistant.components.http import HomeAssistantView

class ESP32ViewAPI(HomeAssistantView):
    """API endpoint for receiving views."""

    url = "/api/esp32_view_creator"
    name = "api:esp32_view_creator"
    requires_auth = True

    async def post(self, request):
        """Handle POST request to receive view data."""
        body = await request.json()
        # Process the view and send to ESP32
        return self.json({"status": "ok"})
