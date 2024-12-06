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
    </style>
</head>
<body>
    <header>
        <span>Remote Builder</span>
        <div>
            <button onclick="alert('Devices clicked!')">Devices</button>
            <button onclick="alert('Settings clicked!')">Settings</button>
        </div>
    </header>
    <main>
        <h1>Hello</h1>
    </main>
</body>
</html>
`;

// Serve the content as an HTML file
document.open();
document.write(content);
document.close();
