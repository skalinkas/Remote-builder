class ESP32ViewBuilder extends HTMLElement {
    set hass(hass) {
        if (!this.content) {
            this.content = document.createElement('div');
            this.appendChild(this.content);
        }
        this.content.innerHTML = `
            <div style="border: 1px solid #ccc; padding: 10px;">
                <h3>ESP32 View Builder</h3>
                <div draggable="true" id="button">Button</div>
                <div id="dropzone" style="border: 1px dashed #000; height: 200px;"></div>
            </div>
        `;
        // Drag and drop logic
    }
}
customElements.define('esp32-view-builder', ESP32ViewBuilder);
