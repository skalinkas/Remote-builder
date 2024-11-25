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

    async addRemote() {
        const name = this.shadowRoot.querySelector("#remote-name").value;
        const host = this.shadowRoot.querySelector("#remote-host").value;

        if (!name || !host) {
            alert("Please fill in all fields.");
            return;
        }

        const response = await fetch("/api/esp32_view_creator/add_remote", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, host }),
        });

        if (response.ok) {
            alert("Remote added successfully!");
            this.fetchRemotes();
        } else {
            alert("Failed to add remote.");
        }
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
                input {
                    margin: 8px 0;
                    padding: 8px;
                    width: calc(100% - 20px);
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
            <h2>Add Remote</h2>
            <input id="remote-name" placeholder="Remote Name" />
            <input id="remote-host" placeholder="Remote Host" />
            <button id="add-remote">Add Remote</button>
        `;

        this.shadowRoot
            .querySelector("#add-remote")
            .addEventListener("click", () => this.addRemote());
    }
}

customElements.define("esp32-view-creator-panel", ESP32ViewCreatorPanel);
