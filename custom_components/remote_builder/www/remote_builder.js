const content = `
<!DOCTYPE html>
<html>
<head>
    <title>Remote Builder</title>
    <style>
        body { font-family: Arial, sans-serif; }
        header { background-color: #03a9f4; color: white; padding: 1em; display: flex; justify-content: space-between; align-items: center; }
        header button { background: none; border: none; color: white; cursor: pointer; padding: 0.5em; font-size: 1em; }
        main { padding: 1em; }
        .placeholder { margin-top: 2em; font-style: italic; }
    </style>
</head>
<body>
    <header>
        <span>Remote Builder</span>
        <div>
            <button onclick="showDevices()">Devices</button>
            <button onclick="showSettings()">Settings</button>
        </div>
    </header>
    <main id="main-content">
        <h1>Hello</h1>
        <div class="placeholder">Click "Devices" to manage remotes or "Settings" to configure the integration.</div>
    </main>
    <script>
        function showDevices() {
            const content = `
                <h1>Devices</h1>
                <p>No devices connected yet. Use the "Add Device" button to connect a new remote.</p>
                <button onclick="alert('Add Device clicked!')">Add Device</button>
            `;
            document.getElementById('main-content').innerHTML = content;
        }

        function showSettings() {
            const content = `
                <h1>Settings</h1>
                <p>Settings page for Remote Builder integration.</p>
            `;
            document.getElementById('main-content').innerHTML = content;
        }
    </script>
</body>
</html>
`;
document.open();
document.write(content);
document.close();
