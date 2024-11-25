class ESP32ViewCreatorPanel extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        this.render();
        this.fetchRemotes();
    }

    async fetchRemotes() {
        const response = await fetch("/api/esp32_view_creator/remotes");
        const remotes = await response.json();
        this.updateRemoteList(remotes);
    }

    updateRemoteList(remotes) {
        const list = this.shadowRoot.querySelector("#remote-list");
        list.innerHTML = remotes
            .map(
                (remote) => `
            <li>${remote.name} (${remote.host})</li>
        `
            )
            .join("");
    }

    render() {
        this.shadowRoot.innerHTML = `
            <style>
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                li {
                    margin: 8px 0;
                }
                button {
                    margin-top: 16px;
                    padding: 8px 16px;
                    font-size: 14px;
                    cursor: pointer;
                }
            </style>
            <h1>ESP32 Remotes</h1>
            <ul id="remote-list"></ul>
            <button id="add-remote">Add Remote</button>
            <button id="flash-esp32">Flash ESP32</button>
        `;

        this.shadowRoot
            .querySelector("#add-remote")
            .addEventListener("click", () => this.addRemote());
        this.shadowRoot
            .querySelector("#flash-esp32")
            .addEventListener("click", () => this.flashESP32());
    }

    addRemote() {
        alert("Add Remote functionality coming soon.");
    }

    flashESP32() {
        window.open("https://esphome.github.io/esp-web-tools/", "_blank");
    }
}

customElements.define("esp32-view-creator-panel", ESP32ViewCreatorPanel);
